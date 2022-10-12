from django.shortcuts import redirect, render
from django.contrib import messages
from factura.forms import FacturaForm
from factura.models import Factura


def facturas(request):
    Facturas = Factura.objects.all()
    print(Facturas)
    return render(request, 'index_factu.html', {'Facturas' : Facturas})

def crearFact(request):
    formulario = FacturaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'La Factura fue creada correctamente.')
        return redirect('factura:Facturas')
            
    return render(request, 'crear_factu.html', {'formulario': formulario})

def eliminarFact(request, id):
    facturas = Factura.objects.get(id_factura=id)
    if facturas.delete():
        messages.warning(request, 'La Factura fue Eliminada correctamente.')
        return redirect('factura:Facturas')
    else:
        messages.error(request, 'Algo salió mal.')
        return redirect('facturas')
