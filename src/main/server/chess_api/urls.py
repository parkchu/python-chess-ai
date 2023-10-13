from django.urls import path
from . import views

urlpatterns = [
    path('move', views.movePiece),
    path('movable-positions/<str:position>', views.getMovablePositions)
]
