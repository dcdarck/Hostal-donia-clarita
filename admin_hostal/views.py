#Código creado por Agustín llaña, Matías Quidel, Jesús Reyes

from xml.dom import ValidationErr
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proveedor, Empleado, Cliente, Huesped
from .forms import EmpleadoEdit, EmpleadoForm, ProveedorEdit, ProveedorForm, ClienteForm, HuespedForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 

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
        messages.success(request, 'El Proveedor fue creado correctamente.')
        return redirect('proveedores')
    else:
        return render(request, 'proveedores/crear_prov.html', {'formulario': formulario})

def editarProv(request, id):
    proveedor = Proveedor.objects.get(id_proveedor=id)
    formulario = ProveedorEdit(request.POST or None, request.FILES or None, instance=proveedor)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request, 'El Proveedor fue modificado correctamente.')
        return redirect('proveedores')
    return render(request, 'proveedores/editar_prov.html', {'formulario': formulario})          

def eliminarProv(request, id):
    proveedores = Proveedor.objects.get(id_proveedor=id) 
    if proveedores.delete():
        messages.warning(request, 'El Proveedor fue Eliminado correctamente.')
        return redirect('proveedores')
    else:
        messages.error(request, 'Algo salió mal.')
        return redirect('proveedores')

def empleados(request):
    Empleados = Empleado.objects.all()
    print(Empleados)
    return render(request, 'empleados/index_emp.html', {'Empleados' : Empleados})

def crearEmp(request):
    formulario = EmpleadoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'El Empleado fue creado correctamente.')
        return redirect('empleados')
            
    return render(request, 'empleados/crear_emp.html', {'formulario': formulario})

def editarEmp(request, id):
    empleados = Empleado.objects.get(id_empleado=id)
    formulario = EmpleadoEdit(request.POST or None, request.FILES or None, instance=empleados)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request, 'El Empleado fue modificado correctamente.')
        return redirect('empleados')
    return render(request, 'empleados/editar_emp.html', {'formulario': formulario})

def eliminarEmp(request, id):
    empleados = Empleado.objects.get(id_empleado=id)
    if empleados.delete():
        messages.warning(request, 'El Empleado fue Eliminado correctamente.')
        return redirect('empleados')
    else:
        messages.error(request, 'Algo salió mal.')
        return redirect('empleados')


def clientes(request):
    Clientes = Cliente.objects.all()
    print(Clientes)
    return render(request, 'clientes/index_cl.html', {'Clientes' : Clientes})


def crearCli(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'El Cliente fue creado correctamente.')
        return redirect('clientes')
    return render(request, 'clientes/crear_cl.html', {'formulario': formulario})

def editarCli(request, id):
    clientes = Cliente.objects.get(id_cliente=id)
    formulario = ClienteForm(request.POST or None, request.FILES or None, instance=clientes)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'El Cliente fue modificado correctamente.')    
        return redirect('clientes')
    return render(request, 'clientes/crear_cl.html', {'formulario': formulario})

def eliminarCli(request, id):
    clientes = Cliente.objects.get(id_cliente=id)
    if clientes.delete():
        messages.warning(request, 'El Cliente fue Eliminado correctamente.')
        return redirect('clientes')
    else:
        messages.error(request, 'Algo salió mal.')
        return redirect('clientes')

def huespedes(request):
    Huespedes = Huesped.objects.all()
    print (Huespedes)
    return render(request, 'huespedes/index_hues.html', {'Huespedes' : Huespedes})

def crearHues(request):
    formulario = HuespedForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'El Huesped fue creado correctamente.')
        return redirect('huespedes')
    return render(request, 'huespedes/crear_hues.html', {'formulario': formulario})

def editarHues(request, id):
    huesped = Huesped.objects.get(id_huesped=id)
    formulario = HuespedForm(request.POST or None, request.FILES or None, instance=huesped)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request, 'El Huesped fue modificado correctamente.')        
        return redirect('huespedes')
    return render(request, 'huespedes/editar_hues.html', {'formulario': formulario})          

def eliminarHues(request, id):
    huespedes = Huesped.objects.get(id_huesped=id)
    if huespedes.delete():
        messages.warning(request, 'El Huesped fue Eliminado correctamente.')
        return redirect('huespedes')
    else:
        messages.error(request, 'Algo salió mal.')
        return redirect('huespedes')