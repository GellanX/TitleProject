from django.urls import path
from . import views

urlpatterns = [
    path('graficos/grafico/', views.ventas_graficos, name='ventas_graficos'),
]