from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models.TipoMypime import TipoMypime
from api.serializers.TipoMypimeSerializer import TipoMypimeSerializer

class TipoMypimeApiView(APIView):

    def get(self, request, id=None):
        if id is not None:
            try:
                tipo_mipyme = TipoMypime.objects.get(id = id)
                serializer = TipoMypimeSerializer(tipo_mipyme)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except TipoMypime.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            tipos_mipymes = TipoMypime.objects.all()
            serializer = TipoMypimeSerializer(tipos_mipymes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post (self, request):
        serializer = TipoMypimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id=None):
        if id is not None:
            try:
                tipo_mipyme = TipoMypime.objects.get(id=id)
                serializer = TipoMypimeSerializer(tipo_mipyme, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
            except TipoMypime.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id is not None:
            try:
                tipo_mipyme = TipoMypime.objects.get(id=id)
                if tipo_mipyme:
                    tipo_mipyme.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            except TipoMypime.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
