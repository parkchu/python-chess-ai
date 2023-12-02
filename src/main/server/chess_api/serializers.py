from rest_framework import serializers
from .models import MoveRequest
from .models import PromoteRequest
from .models import UndoRequest

class MoveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoveRequest
        fields = ("__all__")


class PromoteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoteRequest
        fields = ("__all__")


class UndoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UndoRequest
        fields = ("__all__")
