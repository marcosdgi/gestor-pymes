from rest_framework.serializers import ModelSerializer
from api.models.ActividadPrincipalCNAE import ActividadPrincipalCNAE


class ActividadPrincipalCNAESerializer(ModelSerializer):
    class Meta:
        model = ActividadPrincipalCNAE
        fields = "__all__"