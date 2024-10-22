from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id','name', 'image', 'address', 'description', 'price', 'createdAt', 'noRooms', 'noBath', 'size']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # field to include the currency symbol
        representation['price'] = f"{instance.currency} {instance.price}"
        # field to include 'square meters'
        representation['size'] = f"{instance.size} square meters"
        return representation
