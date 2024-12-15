from django.urls import path
from . import views

urlpatterns = [
    path('graficos/', views.ventas_graficos, name='ventas_graficos'),
]