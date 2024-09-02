from rest_framework.serializers import ModelSerializer
from api.models.Origen import Origen

class OrigenSerializer(ModelSerializer):
    class Meta:
        model = Origen
        fields = '__all__'