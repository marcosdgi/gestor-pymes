from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.OrigenSerializer import OrigenSerializer
from api.models.Origen import Origen
from rest_framework import status


class OrigenApiView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            try:
                obj = Origen.objects.get(id=pk)
                serializer = OrigenSerializer(obj, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Origen.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            actores = Origen.objects.all()
            serializer = OrigenSerializer(actores, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrigenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.error_messages, status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, pk=None):
        if pk is not None:
            obj = Origen.objects.get(id=pk)
            serializer = OrigenSerializer(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(
                    serializer.error_messages, status=status.HTTP_400_BAD_REQUEST
                )

    def delete(self, request, id=None):
        if id is not None:
            obj = Origen.objects.get(id=id)
            if obj:
                obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
