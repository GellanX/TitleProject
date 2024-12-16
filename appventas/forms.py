from django import forms
from django.forms.widgets import DateInput
from django.utils import timezone
from .models import Servicios, Cliente, MetodoPago, Ventas, DetalleVentas, Insumo

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
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].initial = timezone.now()

class DetallesVentasForm(forms.ModelForm):
    class Meta:
        model = DetalleVentas
        fields = ['detalles', 'descripcion', 'precio_detalle', 'fechahora', 'idventas', 'idservicios']
        widgets = {
            'fechahora': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fechahora'].initial = timezone.now()

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

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'descripcion', 'cantidad_disponible', 'precio_unitario']