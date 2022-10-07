from django.urls import path
from empleado import views


urlpatterns = [
    path('empleados', views.empleados, name='empleados'),
    path('empleados/crearEmp', views.crearEmp, name='crearEmp'),
    path('empleados/editarEmp', views.editarEmp, name='editarEmp'),
    path('eliminarEmp/<int:id>', views.eliminarEmp, name='eliminarEmp'),
    path('empleados/editarEmp/<int:id>', views.editarEmp, name='editarEmp'),
]