from rest_framework import serializers
from .models import MoveRequest

class MoveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoveRequest
        fields = ("__all__")
