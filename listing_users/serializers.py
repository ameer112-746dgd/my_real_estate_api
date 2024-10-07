from rest_framework import serializers
from .models import ListingUser

class ListingUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingUser
        fields = '__all__'
