#Código creado por Agustín llaña, Matías Quidel, Jesús Reyes

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Huesped, Proveedor
from .forms import ProveedorForm, HuespedForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
#Proveedores
def proveedores(request):
    Proveedores = Proveedor.objects.all()
    print (Proveedores)
    return render(request, 'proveedores/index_prov.html', {'Proveedores' : Proveedores})

def crearProv(request):
    formulario = ProveedorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('proveedores')
    return render(request, 'proveedores/crear_prov.html', {'formulario': formulario})

def editarProv(request, id):
    proveedor = Proveedor.objects.get(id_proveedor=id)
    formulario = ProveedorForm(request.POST or None, request.FILES or None, instance=proveedor)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('proveedores')
    return render(request, 'proveedores/editar_prov.html', {'formulario': formulario})          

def eliminarProv(request, id):
    proveedores = Proveedor.objects.get(id_proveedor=id)
    proveedores.delete()
    return redirect('proveedores')


def empleados(request):
    return render(request, 'empleados/index_emp.html')    

def clientes(request):
    return render(request, 'clientes/index_cl.html')

#Huespedes

def huespedes(request):
    Huespedes = Huesped.objects.all()
    print (Huespedes)
    return render(request, 'huespedes/index_hues.html', {'Huespedes' : Huespedes})

def crearHues(request):
    formulario = HuespedForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('huespedes')
    return render(request, 'huespedes/crear_hues.html', {'formulario': formulario})

def editarHues(request, id):
    huesped = Huesped.objects.get(id_hue=id)
    formulario = HuespedForm(request.POST or None, request.FILES or None, instance=huesped)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('huespedes')
    return render(request, 'huespedes/editar_hues.html', {'formulario': formulario})          

def eliminarHues(request, id):
    huespedes = Huesped.objects.get(id_hue=id)
    huespedes.delete()
    return redirect('huespedes')