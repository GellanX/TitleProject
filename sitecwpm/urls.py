from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('usuarios/', include('usuarios.urls')),  # Incluye las rutas de la app "usuarios"
    path('appventas/', include('appventas.urls')),
    path('', lambda request: redirect('login', permanent=True)),
    path('graficos/', include('graficos.urls')),
]