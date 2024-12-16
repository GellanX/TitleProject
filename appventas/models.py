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
    cantidad = models.PositiveBigIntegerField(default=0)
    detalles = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio_detalle = models.IntegerField()
    fechahora = models.DateTimeField(default=timezone.now)
    idventas = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    idservicios = models.ForeignKey(Servicios, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.insumo.cantidad_disponible -= self.cantidad
            if self.insumo.cantidad_disponible < 0:
                raise ValueError("No hay suficientes insumos disponibles para esta venta")
            self.insumo.save()
        super().save(*args, **kwargs)

class Insumo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    cantidad_disponible = models.IntegerField(default=0)
    precio_unitario = models.IntegerField(default=0)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre