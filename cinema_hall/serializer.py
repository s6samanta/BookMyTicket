from .models import Hall

from rest_framework import serializers

class HallSerializer(serializers.Serializer):
    class Meta:
        model = Hall
        fields = '__all__'