from rest_framework.serializers import ModelSerializer
from service.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
