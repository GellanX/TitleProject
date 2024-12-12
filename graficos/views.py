import plotly.express as px
from django.shortcuts import render
from appventas.models import Ventas
from django.db.models import Sum

def ventas_graficos(request):
    # Obtener datos agrupados por fecha
    datos = (
        Ventas.objects.values('fecha')
        .annotate(total_ventas=Sum('precioventa'))
        .order_by('fecha')
    )
    
    # Preparar datos para Plotly
    fechas = [dato['fecha'] for dato in datos]
    totales = [dato['total_ventas'] for dato in datos]

    # Crear el gráfico con Plotly
    fig = px.line(
        x=fechas,
        y=totales,
        labels={'x': 'Fecha', 'y': 'Total de Ventas'},
        title='Total de Ventas por Fecha'
    )
    fig.update_layout(template='plotly_white')

    # Convertir el gráfico a HTML
    grafico = fig.to_html(full_html=False)

    return render(request, 'ventas_graficos.html', {'grafico': grafico})



# Create your views here.
