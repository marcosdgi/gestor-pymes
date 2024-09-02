from rest_framework.serializers import ModelSerializer
from api.models.TipoSujeto import TipoSujeto

class TipoSujetoSerializer(ModelSerializer):
    class Meta:
        model = TipoSujeto
        fields = "__all__"