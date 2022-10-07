from django.urls import path
from huesped import views

urlpatterns = [
    path('huespedes', views.huespedes, name='huespedes'),
    path('huespedes/crearHues', views.crearHues, name='crearHues'),
    path('huespedes/editarHues', views.editarHues, name='editarHues'),
    path('eliminarHues/<int:id>', views.eliminarHues, name='eliminarHues'),
    path('huespedes/editarHues/<int:id>', views.editarHues, name='editarHues'),
]
