from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.ActividadPrincipalCNAESerializer import ActividadPrincipalCNAESerializer
from api.models.ActividadPrincipalCNAE import ActividadPrincipalCNAE
from rest_framework import status

class ActividadPrincipalCNAEApiView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            try:
                objs = ActividadPrincipalCNAE.objects.get(id=pk)
                serializer = ActividadPrincipalCNAESerializer(objs, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ActividadPrincipalCNAE.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            obj = ActividadPrincipalCNAE.objects.all()
            serializer = ActividadPrincipalCNAESerializer(obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ActividadPrincipalCNAESerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk = None):
        if pk is not None:
            obj = ActividadPrincipalCNAE.objects.get(id=pk)
            serializer = ActividadPrincipalCNAESerializer(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk = None):
        if pk is not None:
            obj = ActividadPrincipalCNAE.objects.get(id=pk)
            if obj:
                obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

    