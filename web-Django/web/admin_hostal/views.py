from django.shortcuts import render
from django.http import HttpResponse
from .models import Proveedor
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def proveedores(request):
    Proveedores = Proveedor.objects.all()
    print (Proveedores)
    return render(request, 'proveedores/index_prov.html')
def crearProv(request):
    return render(request, 'proveedores/crear_prov.html')
def editarProv(request):
    return render(request, 'proveedores/editar_prov.html')          

def empleados(request):
    return render(request, 'empleados/index_emp.html')    

def clientes(request):
    return render(request, 'clientes/index_cl.html')

def huespedes(request):
    return render(request, 'huespedes/index_hues.html')