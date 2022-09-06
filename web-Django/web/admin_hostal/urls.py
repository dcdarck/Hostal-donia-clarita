from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    
    path('ind_proveedores', views.ind_proveedores, name='ind_proveedores'),
    path('crear_proveedores', views.crear_proveedores, name='crear_proveedores'),

    path('ind_empleados', views.ind_empleados, name='ind_empleados'),
    
    path('ind_huespedes', views.ind_huespedes, name='ind_huespedes'),
    
    path('ind_clientes', views.ind_clientes, name='ind_clientes')
]