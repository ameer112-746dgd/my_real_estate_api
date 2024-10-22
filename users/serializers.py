from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'role', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Normalize role to lowercase
        if 'role' in validated_data:
            validated_data['role'] = validated_data['role'].lower()
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_role(self, value):
        # Ensure the role is valid (case insensitive)
        valid_roles = ['admin', 'user']
        if value.lower() not in valid_roles:
            raise serializers.ValidationError(f'"{value}" is not a valid choice.')
        return value.lower()
