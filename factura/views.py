from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from factura.forms import FacturaForm
from admin_hostal.models import Factura

@login_required(login_url='/login/')
def facturas(request):
    Facturas = Factura.objects.all()
    print(Facturas)
    return render(request, 'index_factu.html', {'Facturas' : Facturas})
 
@login_required(login_url='/login/')
def crearFact(request):
    formulario = FacturaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'La Factura fue creada correctamente.')
        return redirect('factura:Facturas')
            
    return render(request, 'crear_factu.html', {'formulario': formulario})

@login_required(login_url='/login/')
def eliminarFact(request, id):
    facturas = Factura.objects.get(id_factura=id)
    if facturas.delete():
        messages.warning(request, 'La Factura fue Eliminada correctamente.')
        return redirect('factura:Facturas')
    else:
        messages.error(request, 'Algo salió mal.')
        return redirect('facturas')
