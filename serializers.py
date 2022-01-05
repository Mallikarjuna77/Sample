from rest_framework.serializers import ModelSerializer
from.models import Truth
class TruthSerializers(ModelSerializer):
    class Meta:
        model=Truth
        fields="__all__"
