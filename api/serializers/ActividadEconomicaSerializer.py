from rest_framework.serializers import ModelSerializer
from api.models.ActividadesEconomicas import ActividadEconomica

class ActividadEconomicaSerializer(ModelSerializer):
    class Meta:
        model = ActividadEconomica
        fields = "__all__"