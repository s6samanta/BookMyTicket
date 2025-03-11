from .models import User

from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    class meta:
        model = User
        fields = '__all__'