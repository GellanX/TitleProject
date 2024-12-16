from django.urls import path
from .views import lista_servicios, crear_servicio, actualizar_servicio, eliminar_servicio, lista_clientes, crear_cliente, actualizar_cliente, eliminar_cliente, lista_ventas, crear_venta, actualizar_venta, eliminar_venta, lista_detalleventas, crear_detalleventa, actualizar_detalleventa, eliminar_detalleventa, lista_metodopagos, crear_metodopago, actualizar_metodopago, eliminar_metodopago, registrar_venta, home
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('servicios/', lista_servicios, name='lista_servicios'),
    path('servicios/crear/', crear_servicio, name='crear_servicio'),
    path('servicios/actualizar/<int:id>/', actualizar_servicio, name='actualizar_servicio'),
    path('servicios/eliminar/<int:id>/', eliminar_servicio, name='eliminar_servicio'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/crear/', crear_cliente, name='crear_cliente'),
    path('clientes/actualizar/<int:id>/', actualizar_cliente, name='actualizar_cliente'),
    path('clientes/eliminar/<int:id>/', eliminar_cliente, name='eliminar_cliente'),
    path('ventas/', lista_ventas, name='lista_ventas'),
    path('ventas/crear/', crear_venta, name='crear_venta'),
    path('ventas/actualizar/<int:id>/', actualizar_venta, name='actualizar_venta'),
    path('ventas/eliminar/<int:id>/', eliminar_venta, name='eliminar_venta'),
    path('detalleventas/', lista_detalleventas, name='lista_detalleventas'),
    path('detalleventas/crear/', crear_detalleventa, name='crear_detalleventa'),
    path('detalleventas/actualizar/<int:id>/', actualizar_detalleventa, name='actualizar_detalleventa'),
    path('detalleventas/eliminar/<int:id>/', eliminar_detalleventa, name='eliminar_detalleventa'),
    path('metodopagos/', lista_metodopagos, name='lista_metodopagos'),
    path('metodopagos/crear/', crear_metodopago, name='crear_metodopago'),
    path('metodopagos/actualizar/<int:id>/', actualizar_metodopago, name='actualizar_metodopago'),
    path('metodopagos/eliminar/<int:id>/', eliminar_metodopago, name='eliminar_metodopago'),
    path('ventas/registrar/', registrar_venta, name='registrar_venta'),
    path('insumos/', views.listar_insumos, name='lista_insumos'),
    path('insumos/agregar/', views.agregar_insumo, name='agregar_insumo'),
    path('insumos/editar/<int:insumo_id>/', views.editar_insumo, name='editar_insumo'),
    path('insumos/eliminar/<int:insumo_id>/', views.eliminar_insumo, name='eliminar_insumo'),
    path('base/', views.base_view, name='base'),
    path('', home, name='home'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
]