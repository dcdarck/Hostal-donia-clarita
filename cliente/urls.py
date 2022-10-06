from django.urls import path
from cliente import views

urlpatterns = [
    path('clientes', views.clientes, name='clientes'),
    path('clientes/crearCli', views.crearCli, name='crearCli'),
    path('clientes/editarCli', views.editarCli, name='editarCli'),
    path('eliminarCli/<int:id>', views.eliminarCli, name='eliminarCli'),
    path('clientes/editarCli/<int:id>',  views.editarCli, name='editarCli'),
]
