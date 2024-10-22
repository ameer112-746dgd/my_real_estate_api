from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        read_only_fields = ['created_by']  # Make created_by read-only
