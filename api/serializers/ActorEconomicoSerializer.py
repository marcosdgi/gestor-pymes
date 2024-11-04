from rest_framework.serializers import ModelSerializer
from api.models.ActividadPrincipalCNAE import ActividadPrincipalCNAE
from api.models.ActividadesEconomicas import ActividadEconomica
from api.models.ActorEconomico import ActorEconomico
from api.models.Denominacion import Denominacion
from api.models.Origen import Origen
from api.models.SectorEconomico import SectorEconomico
from api.models.Solicitante import Solicitante
from api.models.TipoMypime import TipoMypime
from api.models.TipoSujeto import TipoSujeto
from .TipoMypimeSerializer import TipoMypimeSerializer
from .DenominacionSerializer import DenominacionSerializer
from .TipoSujetoSerializer import TipoSujetoSerializer
from .ActividadPrincipalCNAESerializer import ActividadPrincipalCNAESerializer
from .SectorEconomicoSerializer import SectorEconomicoSerializer
from .ActividadEconomicaSerializer import ActividadEconomicaSerializer
from .SolicitanteSerializer import SolicitanteSerializer
from .OrigenSerializer import OrigenSerializer
from rest_framework import serializers
class ActorEconomicoSerializer(ModelSerializer):
    
    class Meta:
        model = ActorEconomico
        fields = '__all__'
    
    #### Relaciones ####
    tipoMypime = TipoMypimeSerializer(source='tipo_mypime_id')
    denominacion = DenominacionSerializer(source='denominacion_id')
    tipoSujeto = TipoSujetoSerializer(source='tipo_sujeto_id')
    actividadEconomicaPrincipal = ActividadPrincipalCNAESerializer(source='actividad_economica_principal_id')
    sectorEconomico = SectorEconomicoSerializer(source='sector_economico_id')
    actividadEconomicaPrincipalCNAE = ActividadEconomicaSerializer(source='actividad_principal_CNAE_id')
    solicitante = SolicitanteSerializer(source="solicitante_id")
    origen = OrigenSerializer(source="origen_id")

class ActorEconomicoCreationSerializer(ModelSerializer):
    
    tipo_mypime_id = serializers.PrimaryKeyRelatedField(
        queryset=TipoMypime.objects.all(),
    )
    denominacion_id = serializers.PrimaryKeyRelatedField(
        queryset=Denominacion.objects.all(),
    )
    tipo_sujeto_id = serializers.PrimaryKeyRelatedField(
        queryset=TipoSujeto.objects.all(),
    )
    actividad_principal_CNAE_id = serializers.PrimaryKeyRelatedField(
        queryset=ActividadPrincipalCNAE.objects.all(),
    )
    sector_economico_id = serializers.PrimaryKeyRelatedField(
        queryset=SectorEconomico.objects.all(),
    )
    actividad_economica_principal_id = serializers.PrimaryKeyRelatedField(
        queryset=ActividadEconomica.objects.all(),
    )
    
    solicitante_id = serializers.PrimaryKeyRelatedField(
        queryset=Solicitante.objects.all(),
    )
    origen_id = serializers.PrimaryKeyRelatedField(
        queryset=Origen.objects.all(),
    )

    class Meta:
        model = ActorEconomico
        fields = '__all__'