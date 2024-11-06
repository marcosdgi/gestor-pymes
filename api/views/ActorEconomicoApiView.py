from rest_framework.views import APIView
from rest_framework.response import Response
from api.models.ActividadesEconomicas import ActividadEconomica
from api.serializers.ActorEconomicoSerializer import (
    ActorEconomicoCreationSerializer,
    ActorEconomicoSerializer,
)
from api.models.ActorEconomico import ActorEconomico
from rest_framework import status
from api.filters.ActorEconomicoFilter import ActorEconomicoFilter
from rest_framework.pagination import PageNumberPagination


class ActorEconomicoPagination(PageNumberPagination):
    page_size = 10


class ActorEconomicoApiView(APIView):
    pagination_class = ActorEconomicoPagination

    def get(self, request, pk=None):
        if pk is not None:
            try:
                actor = ActorEconomico.objects.get(id=pk)
                actor_serializer = ActorEconomicoSerializer(actor, many=False)
                return Response(actor_serializer.data, status=status.HTTP_200_OK)
            except ActorEconomico.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = ActorEconomico.objects.all()
            filterset = ActorEconomicoFilter(request.GET, queryset=queryset)
            if filterset.is_valid():
                queryset = filterset.qs
            serializer = ActorEconomicoSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
            # queryset = ActorEconomico.objects.all()
            # filterset = ActorEconomicoFilter(request.GET, queryset=queryset)
            # if filterset.is_valid():
            #     queryset = filterset.qs

            # # Paginación
            # paginator = ActorEconomicoPagination()
            # paginated_queryset = paginator.paginate_queryset(queryset, request)
            # serializer = ActorEconomicoSerializer(paginated_queryset, many=True)
            # return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ActorEconomicoCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if pk is not None:
            actor = ActorEconomico.objects.get(id=pk)
            serializer = ActorEconomicoCreationSerializer(actor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is not None:
            actor = ActorEconomico.objects.get(id=pk)
            if actor:
                actor.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
