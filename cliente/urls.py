from django.urls import path
from .views import listarClientes, editarCliente, nuevoCliente, eliminarCliente

urlpatterns = [
    path('clientes/', listarClientes.as_view(), name='listaClientes'),
    path('clientes/nuevo', nuevoCliente.as_view(), name='nuevoCliente'),
    path('clientes/editar/<int:pk>', editarCliente.as_view(), name='editarCliente'),
    path('clientes/eliminar/<int:pk>', eliminarCliente.as_view(), name='eliminarCliente')
]
