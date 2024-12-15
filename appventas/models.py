from django.db import models
from django.utils import timezone

# Create your models here.
class Servicios(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    activo = models.BooleanField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    convenio = models.CharField(max_length=60)
    rut = models.CharField(max_length=12)
    email = models.CharField(max_length=60)

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=30)

class Ventas(models.Model):
    codigo = models.CharField(max_length=10)
    precioventa = models.IntegerField()
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField(default=timezone.now)
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idmetodopago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)

class DetalleVentas(models.Model):
    detalles = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio_detalle = models.IntegerField()
    fechahora = models.DateTimeField(default=timezone.now)
    idventas = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    idservicios = models.ForeignKey(Servicios, on_delete=models.CASCADE)