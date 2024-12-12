from django import forms
from .models import Servicios, Cliente, MetodoPago, Ventas, DetalleVentas

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ['nombre', 'descripcion', 'activo']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'convenio', 'rut', 'email']

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ['nombre']

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['codigo', 'precioventa', 'nombre', 'descripcion', 'fecha', 'idcliente', 'idmetodopago']

class DetallesVentasForm(forms.ModelForm):
    class Meta:
        model = DetalleVentas
        fields = ['detalles', 'descripcion', 'precio_detalle', 'fechahora', 'idventas', 'idservicios']

class RegistroVentaForm(forms.ModelForm):
    servicios = forms.ModelMultipleChoiceField(
        queryset=Servicios.objects.filter(activo=True),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Servicios"
    )

    class Meta:
        model = Ventas
        fields = ['codigo', 'precioventa', 'nombre', 'descripcion', 'fecha', 'idcliente', 'idmetodopago']