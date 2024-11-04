from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.ActividadEconomicaSerializer import ActividadEconomicaSerializer
from api.models.ActividadesEconomicas import ActividadEconomica
from rest_framework import status
from api.filters.ActividadEconomicaFilter import ActividadEconomicaFilter
class ActividadEconominaApiView(APIView):

    def get(self, request, pk=None, code=None):
        if pk  :
            try:
                objs = ActividadEconomica.objects.get(id=pk)
                serializer = ActividadEconomicaSerializer(objs, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ActividadEconomica.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
        elif code:
            try:
                objs = ActividadEconomica.objects.filter(codigo=code)
                serializer = ActividadEconomicaSerializer(objs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ActividadEconomica.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            queryset = ActividadEconomica.objects.all()
            filterset = ActividadEconomicaFilter(request.GET, queryset=queryset)
            if filterset.is_valid():
                queryset = filterset.qs
            serializer = ActividadEconomicaSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ActividadEconomicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk = None):
        if pk is not None:
            obj = ActividadEconomica.objects.get(id=pk)
            serializer = ActividadEconomicaSerializer(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk = None):
        if pk is not None:
            obj = ActividadEconomica.objects.get(id=pk)
            if obj:
                obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

