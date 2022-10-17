from django.shortcuts import redirect, render
from proveedor.forms import ProveedorEdit, ProveedorEdit
from django.contrib import messages
from admin_hostal.models import Proveedor
from proveedor.forms import ProveedorForm

def proveedores(request):
    Proveedores = Proveedor.objects.all()
    print (Proveedores)
    return render(request, 'index_prov.html', {'Proveedores' : Proveedores})


def crearProv(request):
    formulario = ProveedorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'El Proveedor fue creado correctamente.')
        return redirect('proveedor:proveedores')
    else:
        return render(request, 'crear_prov.html', {'formulario': formulario})

def editarProv(request, id):
    proveedor = Proveedor.objects.get(id_proveedor=id)
    formulario = ProveedorEdit(request.POST or None, request.FILES or None, instance=proveedor)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request, 'El Proveedor fue modificado correctamente.')
        return redirect('proveedor:proveedores')
    return render(request, 'editar_prov.html', {'formulario': formulario})          

def eliminarProv(request, id):
    proveedores = Proveedor.objects.get(id_proveedor=id) 
    if proveedores.delete():
        messages.warning(request, 'El Proveedor fue Eliminado correctamente.')
        return redirect('proveedor:proveedores')
    else:
        messages.error(request, 'Algo salió mal.')
        return redirect('proveedor:proveedores')