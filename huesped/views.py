from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from bases.views import SinPrivilegios
from admin_hostal.models import Huesped
from .forms import HuespedForm

@login_required(login_url='/login/')   
def huespedes(request):
    Huespedes = Huesped.objects.all()
    print (Huespedes)
    return render(request, 'index_hues.html', {'Huespedes' : Huespedes})

@login_required(login_url='/login/')
def crearHues(request):
    formulario = HuespedForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'El Huesped fue creado correctamente.')
        return redirect('huesped:huespedes')
    return render(request, 'crear_hues.html', {'formulario': formulario})

@login_required(login_url='/login/')
def editarHues(request, id):
    huesped = Huesped.objects.get(id_huesped=id)
    formulario = HuespedForm(request.POST or None, request.FILES or None, instance=huesped)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request, 'El Huesped fue modificado correctamente.')        
        return redirect('huesped:huespedes')
    return render(request, 'editar_hues.html', {'formulario': formulario})          

@login_required(login_url='/login/')
def eliminarHues(request, id):
    huespedes = Huesped.objects.get(id_huesped=id)
    if huespedes.delete():
        messages.warning(request, 'El Huesped fue Eliminado correctamente.')
        return redirect('huesped:huespedes')
    else:
        messages.error(request, 'Algo salió mal.')
        return redirect('huesped:huespedes')