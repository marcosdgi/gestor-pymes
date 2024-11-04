from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models.Denominacion import Denominacion
from api.serializers.DenominacionSerializer import DenominacionSerializer

class DenomacionAPIView(APIView):
    # permission_classes=[all]
    def get(self, request, id=None):
        if id is not None:
            try:
                obj = Denominacion.objects.get(id = id)
                serializer = DenominacionSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Denominacion.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            objs = Denominacion.objects.all()
            serializer = DenominacionSerializer(objs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post (self, request):
        serializer = DenominacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id=None):
        if id is not None:
            try:
                obj = Denominacion.objects.get(id=id)
                serializer = DenominacionSerializer(obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
            except Denominacion.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id is not None:
            try:
                obj = Denominacion.objects.get(id=id)
                if obj:
                    obj.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            except Denominacion.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)