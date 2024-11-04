from rest_framework.serializers import ModelSerializer
from api.models.Denominacion import Denominacion


class DenominacionSerializer(ModelSerializer):
    class Meta:
        model = Denominacion
        fields = '__all__'