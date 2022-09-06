from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('proveedores', views.proveedores, name='proveedores'),
    path('empleados', views.empleados, name='empleados'),
    path('huespedes', views.huespedes, name='huespedes'),
    path('clientes', views.clientes, name='clientes')
]