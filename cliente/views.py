from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from bases.views import SinPrivilegios
from .models import Cliente
from .forms import ClienteForm

    
def crearCli(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'El Cliente fue creado correctamente.')
        return redirect('cliente:clientes')
    return render(request, 'crear_cl.html', {'formulario': formulario})

def clientes(request):
    Clientes = Cliente.objects.all()
    print(Clientes)
    return render(request, 'index_cl.html', {'Clientes' : Clientes})


def crearCli(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'El Cliente fue creado correctamente.')
        return redirect('cliente:clientes')
    return render(request, 'crear_cl.html', {'formulario': formulario})

def editarCli(request, id):
    clientes = Cliente.objects.get(id_cliente=id)
    formulario = ClienteForm(request.POST or None, request.FILES or None, instance=clientes)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'El Cliente fue modificado correctamente.')    
        return redirect('cliente:clientes')
    return render(request, 'crear_cl.html', {'formulario': formulario})

def eliminarCli(request, id):
    clientes = Cliente.objects.get(id_cliente=id)
    if clientes.delete():
        messages.warning(request, 'El Cliente fue Eliminado correctamente.')
        return redirect('cliente:clientes')
    else:
        messages.error(request, 'Algo salió mal.')
        return redirect('cliente:clientes')