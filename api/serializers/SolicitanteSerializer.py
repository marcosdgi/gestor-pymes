from rest_framework.serializers import ModelSerializer
from api.models.Solicitante import Solicitante
from api.models.TipoMypime import TipoMypime
from .TipoMypimeSerializer import TipoMypimeSerializer
from rest_framework import serializers


class SolicitanteSerializer(ModelSerializer):

    class Meta:
        model = Solicitante
        fields = "__all__"

    tipo_mipyme = TipoMypimeSerializer(source="tipo_mipyme_id")


class SolicitanteCreationSerializer(ModelSerializer):

    class Meta:
        model = Solicitante
        fields = "__all__"

    tipo_mipyme_id = serializers.PrimaryKeyRelatedField(
        queryset=TipoMypime.objects.all(),
    )
