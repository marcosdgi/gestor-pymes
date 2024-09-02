from rest_framework.serializers import ModelSerializer
from api.models.SectorEconomico import SectorEconomico
class SectorEconomicoSerializer(ModelSerializer):
    class Meta:
        model = SectorEconomico
        fields = '__all__'