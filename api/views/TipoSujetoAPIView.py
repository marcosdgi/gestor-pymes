from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models.TipoSujeto import TipoSujeto
from api.serializers.TipoSujetoSerializer import TipoSujetoSerializer

class TipoSujetoApiView(APIView):

    def get(self, request, id=None):
        if id is not None:
            try:
                obj = TipoSujeto.objects.get(id = id)
                serializer = TipoSujetoSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except TipoSujeto.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            objs = TipoSujeto.objects.all()
            serializer = TipoSujetoSerializer(objs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post (self, request):
        serializer = TipoSujetoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id=None):
        if id is not None:
            try:
                obj = TipoSujeto.objects.get(id=id)
                serializer = TipoSujetoSerializer(obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
            except TipoSujeto.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id is not None:
            try:
                obj = TipoSujeto.objects.get(id=id)
                if obj:
                    obj.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            except TipoSujeto.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
