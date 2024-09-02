from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.SolicitanteSerializer import SolicitanteSerializer
from api.models.Solicitante import Solicitante
from rest_framework import status

class SolicitanteApiView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            try:
                obj = Solicitante.objects.get(id=pk)
                serializer = SolicitanteSerializer(obj, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Solicitante.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            actores = Solicitante.objects.all()
            serializer = SolicitanteSerializer(actores, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SolicitanteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id = None):
        if id is not None:
            obj = Solicitante.objects.get(id=id)
            serializer = SolicitanteSerializer(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id = None):
        if id is not None:
            obj = Solicitante.objects.get(id=id)
            if obj:
                obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

    