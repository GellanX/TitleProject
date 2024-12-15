import plotly.express as px
from django.shortcuts import render
from appventas.models import Ventas
from django.db.models import Sum

def ventas_graficos(request):
    datos = (
        Ventas.objects.values('fecha')
        .annotate(total_ventas=Sum('precioventa'))
        .order_by('fecha')
    )
    
    fechas = [dato['fecha'] for dato in datos]
    totales = [dato['total_ventas'] for dato in datos]

    fig = px.line(
        x=fechas,
        y=totales,
        labels={'x': 'Fecha', 'y': 'Total de Ventas'},
        title='Total de Ventas por Fecha'
    )
    fig.update_layout(template='plotly_white')

    fig2 = px.bar(
        Ventas.objects.all().values('idcliente__nombre').annotate(total=Sum('precioventa')),
        x='idcliente__nombre',
        y='total',
        title='Ventas por Cliente',
        labels={'idcliente__nombre': 'Cliente', 'total': 'Total Ventas'}
    )


    grafico = fig.to_html(full_html=False)
    grafico2 = fig2.to_html(full_html=False)

    return render(request, 'ventas_graficos.html', {'grafico': grafico, 'grafico2': grafico2})



# Create your views here.
