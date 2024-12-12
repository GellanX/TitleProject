from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Servicios, Cliente, MetodoPago, Ventas, DetalleVentas
from .forms import ServiciosForm, ClienteForm, MetodoPagoForm, VentasForm, DetallesVentasForm, RegistroVentaForm

# Create your views here.
# CRUD Servicios
def lista_servicios(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios/lista.html', {'servicios': servicios})

def crear_servicio(request):
    form = ServiciosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_servicios')
    return render(request, 'servicios/formulario.html', {'form': form})

def actualizar_servicio(request, id):
    servicio = get_object_or_404(Servicios, id=id)
    form = ServiciosForm(request.POST or None, instance=servicio)
    if form.is_valid():
        form.save()
        return redirect('lista_servicios')
    return render(request, 'servicios/formulario.html', {'form': form})

def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicios, id=id)
    if request.method == 'POST':
        servicio.delete()
        return redirect('lista_servicios')
    return render(request, 'servicios/eliminar.html', {'servicio': servicio})

#CRUD Clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listacliente.html', {'clientes': clientes})

def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'clientes/formulariocliente.html', {'form': form})

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'clientes/formulariocliente.html', {'form': form})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/eliminarcliente.html', {'cliente': cliente})

#CRUD Ventas
@login_required
def lista_ventas(request):
    ventas = Ventas.objects.select_related('idcliente', 'idmetodopago').all()
    return render(request, 'ventas/listaventa.html', {'ventas': ventas})

def crear_venta(request):
    form = VentasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_ventas')
    return render(request, 'ventas/formularioventa.html', {'form': form})

def actualizar_venta(request, id):
    venta = get_object_or_404(Servicios, id=id)
    form = VentasForm(request.POST or None, instance=venta)
    if form.is_valid():
        form.save()
        return redirect('lista_ventas')
    return render(request, 'ventas/formularioventa.html', {'form': form})

def eliminar_venta(request, id):
    venta = get_object_or_404(Ventas, id=id)
    if request.method == 'POST':
        venta.delete()
        return redirect('lista_ventas')
    return render(request, 'ventas/eliminarventa.html', {'venta': venta})

#CRUD DetalleVentas
def lista_detalleventas(request):
    detalleventas = DetalleVentas.objects.all()
    return render(request, 'detalleventas/listadetalleventa.html', {'detalleventas': detalleventas})

def crear_detalleventa(request):
    form = DetallesVentasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_detalleventas')
    return render(request, 'detalleventas/formulariodetalleventa.html', {'form': form})

def actualizar_detalleventa(request, id):
    detalleventa = get_object_or_404(DetalleVentas, id=id)
    form = DetallesVentasForm(request.POST or None, instance=detalleventa)
    if form.is_valid():
        form.save()
        return redirect('lista_detalleventas')
    return render(request, 'detalleventas/formulariodetalleventa.html', {'form': form})

def eliminar_detalleventa(request, id):
    detalleventa = get_object_or_404(DetalleVentas, id=id)
    if request.method == 'POST':
        detalleventa.delete()
        return redirect('lista_detalleventas')
    return render(request, 'detalleventas/eliminardetalleventa.html', {'detalleventa': detalleventa})

#CRUD MetodoPago
def lista_metodopagos(request):
    metodopagos = MetodoPago.objects.all()
    return render(request, 'metodopagos/listametodopago.html', {'metodopagos': metodopagos})

def crear_metodopago(request):
    form = MetodoPagoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_metodopagos')
    return render(request, 'metodopagos/formulariometodopago.html', {'form': form})

def actualizar_metodopago(request, id):
    metodopago = get_object_or_404(MetodoPago, id=id)
    form = MetodoPagoForm(request.POST or None, instance=metodopago)
    if form.is_valid():
        form.save()
        return redirect('lista_metodopagos')
    return render(request, 'metodopagos/formulariometodopago.html', {'form': form})

def eliminar_metodopago(request, id):
    metodopago = get_object_or_404(MetodoPago, id=id)
    if request.method == 'POST':
        metodopago.delete()
        return redirect('lista_metodopagos')
    return render(request, 'metodopagos/eliminarmetodopago.html', {'metodopago': metodopago})

#Registro de Ventas
@login_required
def registrar_venta(request):
    if request.method == 'POST':
        form = RegistroVentaForm(request.POST)
        if form.is_valid():
            # Guardar la venta
            venta = form.save()

                        # Guardar detalles de venta por servicio
            servicios = form.cleaned_data['servicios']
            for servicio in servicios:
                DetalleVentas.objects.create(
                    detalles=f"Detalle de {servicio.nombre}",
                    descripcion=servicio.descripcion,
                    precio_detalle=servicio.precioventa,  # Con esto ajustas según los precios colocados
                    fechahora=venta.fecha,
                    idventas=venta,
                    idservicios=servicio
                )
            return redirect('lista_ventas')  # Redirige a una página de lista de ventas, que puedes crear   
    else:
        form = RegistroVentaForm()
    return render(request, 'ventas/registrar.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')
