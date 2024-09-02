from rest_framework.serializers import ModelSerializer
from api.models.Solicitante import Solicitante
from .TipoMypimeSerializer import TipoMypimeSerializer

class SolicitanteSerializer( ModelSerializer ):

    class Meta:
        model = Solicitante
        fields = '__all__'

    tipo_mipyme = TipoMypimeSerializer(source='tipo_mipyme_id')