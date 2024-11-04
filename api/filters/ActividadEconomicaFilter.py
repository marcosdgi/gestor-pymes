from django_filters import FilterSet
from api.models.ActividadesEconomicas import ActividadEconomica

class ActividadEconomicaFilter(FilterSet):
    class Meta:
        model = ActividadEconomica
        fields = ['codigo', 'nombre']