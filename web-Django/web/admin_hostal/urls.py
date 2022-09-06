from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    
    path('proveedores', views.proveedores, name='proveedores'),
    path('proveedores/crearProv', views.crearProv, name='crearProv'),

    path('ind_empleados', views.ind_empleados, name='ind_empleados'),
    
    path('ind_huespedes', views.ind_huespedes, name='ind_huespedes'),
    
    path('ind_clientes', views.ind_clientes, name='ind_clientes')
]