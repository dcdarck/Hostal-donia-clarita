#Código creado por Agustín llaña, Matías Quidel, Jesús Reyes
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    
    path('proveedores', views.proveedores, name='proveedores'),
    path('proveedores/crearProv', views.crearProv, name='crearProv'),
    path('proveedores/editarProv', views.editarProv, name='editarProv'),
    path('eliminarProv/<int:id>', views.eliminarProv, name='eliminarProv'),
    path('proveedores/editarProv/<int:id>', views.editarProv, name='editarProv'),

    path('empleados', views.empleados, name='empleados'),
    path('empleados/crearEmp', views.crearEmp, name='crearEmp'),
    path('empleados/editarEmp', views.editarEmp, name='editarEmp'),
    path('eliminarEmp/<int:id>', views.eliminarEmp, name='eliminarEmp'),
    path('empleados/editarEmp/<int:id>', views.editarEmp, name='editarEmp'),
    
    path('huespedes', views.huespedes, name='huespedes'),
    path('huespedes/crearHues', views.crearHues, name='crearHues'),
    path('huespedes/editarHues', views.editarHues, name='editarHues'),
    path('eliminarHues/<int:id>', views.eliminarHues, name='eliminarHues'),
    path('huespedes/editarHues/<int:id>', views.editarHues, name='editarHues'),

    path('clientes', views.clientes, name='clientes'),
    path('clientes/crearCli', views.crearCli, name='crearCli'),
    path('clientes/editarCli', views.editarCli, name='editarCli'),
    path('eliminarCli/<int:id>', views.eliminarCli, name='eliminarCli'),
    path('clientes/editarCli/<int:id>',  views.editarCli, name='editarCli'),
]