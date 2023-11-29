from django.db import models

# Create your models here.

class MoveRequest(models.Model):
    currentPosition = models.CharField(max_length=2)
    targetPosition = models.CharField(max_length=2)


class PromoteRequest(models.Model):
    position = models.CharField(max_length=2)
    pieceType = models.CharField(max_length=8)
    