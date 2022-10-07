from django.urls import path
from proveedor import views

urlpatterns = [
    path('proveedores', views.proveedores, name='proveedores'),
    path('proveedores/crearProv', views.crearProv, name='crearProv'),
    path('proveedores/editarProv', views.editarProv, name='editarProv'),
    path('eliminarProv/<int:id>', views.eliminarProv, name='eliminarProv'),
    path('proveedores/editarProv/<int:id>', views.editarProv, name='editarProv'),
]