from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from bases.views import SinPrivilegios
from .models import Cliente
from .forms import ClienteForm


class listarClientes(SinPrivilegios, generic.ListView):
    permission_required = "cliente.view_cliente"
    model = Cliente
    template_name = "listaClientes.html"
    context_object_name = "clientes"


class editarCliente(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Cliente
    template_name = "formCliente.html"
    context_object_name = "cliente"
    form_class = ClienteForm
    success_url = reverse_lazy("cliente:listaClientes")
    success_message = "La categoría ha sido actualizada correctamente"
    permission_required = "cliente.change_cliente"

    def form_valid(self, form):
        form.instance.usuarioModifica = self.request.user.id

        return super().form_valid(form)


class eliminarCliente(SuccessMessageMixin, SinPrivilegios, generic.DeleteView):
    model = Cliente
    template_name = 'eliminarCliente.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("cliente:listaClientes")
    success_message = "El Cliente ha sido eliminado correctamente"
    permission_required = "cliente.delete_cliente"
    
class nuevoCliente(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Cliente
    template_name = "formCliente.html"
    context_object_name = "cliente"
    form_class = ClienteForm
    success_url = reverse_lazy("cliente:listaClientes")
    success_message = "El cliente se ha creado correctamente"
    permission_required = "cliente.add_cliente"

    def form_valid(self, form):
        form.instance.usuarioCrea = self.request.user

        return super().form_valid(form)