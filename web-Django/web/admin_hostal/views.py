from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def ind_proveedores(request):
    return render(request, 'proveedores/index_prov.html')
def crear_proveedores(request):
    return render(request, 'proveedores/crear_prov.html')    

def ind_empleados(request):
    return render(request, 'empleados/index_emp.html')    

def ind_clientes(request):
    return render(request, 'clientes/index_cl.html')

def ind_huespedes(request):
    return render(request, 'huespedes/index_hues.html')