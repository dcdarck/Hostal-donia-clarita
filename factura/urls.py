from django.urls import path
from factura import views


urlpatterns = [
    path('facturas', views.facturas, name='facturas'),
    path('facturas/crearFact', views.crearFact, name='crearFact'),
]