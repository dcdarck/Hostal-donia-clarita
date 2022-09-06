from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def proveedores(request):
    return render(request, 'proveedores/index.html')
def empleados(request):
    return render(request, 'empleados/index.html')    
def clientes(request):
    return render(request, 'clientes/index.html')
def huespedes(request):
    return render(request, 'huespedes/index.html')