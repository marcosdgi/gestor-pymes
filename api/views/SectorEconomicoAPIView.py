from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models.SectorEconomico import SectorEconomico
from api.serializers.SectorEconomicoSerializer import SectorEconomicoSerializer

class SectorEconomicoApiview(APIView):

    def get(self, request, id=None):
        if id is not None:
            try:
                sector = SectorEconomico.objects.get(id = id)
                serializer = SectorEconomicoSerializer(sector)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except SectorEconomico.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            sectores = SectorEconomico.objects.all()
            serializer = SectorEconomicoSerializer(sectores, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post (self, request):
        serializer = SectorEconomicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id=None):
        if id is not None:
            try:
                sector = SectorEconomico.objects.get(id=id)
                serializer = SectorEconomicoSerializer(sector, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
            except SectorEconomico.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id is not None:
            try:
                sector = SectorEconomico.objects.get(id=id)
                if sector:
                    sector.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            except SectorEconomico.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)