from django.contrib import admin
from appventas.models import Cliente, Servicios, MetodoPago, Ventas, DetalleVentas

admin.site.register(Cliente)
admin.site.register(Servicios)
admin.site.register(MetodoPago)
admin.site.register(Ventas)
admin.site.register(DetalleVentas)

# Register your models here.
