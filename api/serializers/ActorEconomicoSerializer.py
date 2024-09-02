from rest_framework.serializers import ModelSerializer
from api.models.ActorEconomico import ActorEconomico
from .TipoMypimeSerializer import TipoMypimeSerializer
from .DenominacionSerializer import DenominacionSerializer
from .TipoSujetoSerializer import TipoSujetoSerializer
from .ActividadPrincipalCNAESerializer import ActividadPrincipalCNAESerializer
from .SectorEconomicoSerializer import SectorEconomicoSerializer
from .ActividadEconomicaSerializer import ActividadEconomicaSerializer


class ActorEconomicoSerializer(ModelSerializer):
    
    class Meta:
        model = ActorEconomico
        fields = '__all__'
    
    #### Relaciones ####
    tipo_mypime = TipoMypimeSerializer(source='tipo_mypime_id')
    denominacion = DenominacionSerializer(source='denominacion_id')
    tipo_sujeto = TipoSujetoSerializer(source='tipo_sujeto_id')
    actividad_economica_principal = ActividadPrincipalCNAESerializer(source='actividad_economica_principal_id')
    sector_economico = SectorEconomicoSerializer(source='sector_economico_id')
    actividad_principal_CNAE = ActividadEconomicaSerializer(source='actividad_principal_CNAE_id')