from rest_framework import serializers
from .models import MoveRequest
from .models import PromoteRequest

class MoveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoveRequest
        fields = ("__all__")


class PromoteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoteRequest
        fields = ("__all__")
