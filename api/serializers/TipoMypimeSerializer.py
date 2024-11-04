from rest_framework.serializers import ModelSerializer
from api.models.TipoMypime import TipoMypime

class TipoMypimeSerializer(ModelSerializer):
    class Meta:
        model = TipoMypime
        fields = "__all__"