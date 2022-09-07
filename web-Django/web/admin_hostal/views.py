#Código creado por Agustín llaña, Matías Quidel, Jesús Reyes

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proveedor, Empleado, Cliente, Huesped
from .forms import EmpleadoForm, ProveedorForm, ClienteForm, HuespedForm
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
    empleados = Empleado.objects.all()
    print(empleados)
    return render(request, 'empleados/index_emp.html')

def crearEmp(request):
    formulario = EmpleadoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('empleados')
    return render(request, 'empleados/crear_emp.html', {'formulario': formulario})

def editarEmp(request, id):
    empleados = Empleado.objects.get(id_empleado=id)
    formulario = EmpleadoForm(request.POST or None, request.FILES or None, instance=empleados)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('empleados')
    return render(request, 'empleados/editar_emp.html', {'formulario': formulario})

def eliminarEmp(request, id):
    empleados = Empleado.objects.get(id_empleado=id)
    empleados.delete()
    return redirect('empleados')


def clientes(request):
    clientes = Cliente.objects.all()
    print(clientes)
    return render(request, 'clientes/index_cl.html')

def crearCli(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/crear_cli.html', {'formulario': formulario})

def editarCli(request):
    clientes = Cliente.objects.get(id_cliente=id)
    formulario = ClienteForm(request.POST or None, request.FILES or None, instance=clientes)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/crear_cli.html', {'formulario': formulario})

def eliminarCli(request):
    clientes = Cliente.objects.get(id_cliente=id)
    clientes.delete()
    return redirect('clientes')

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