from django.db import models

# Create your models here.

class Proveedor(models.Model):
    id_proveedor  = models.AutoField(primary_key=True)
    nombre_prov = models.CharField(max_length=100, verbose_name='Nombre', null=True)
    email = models.CharField(max_length=100, verbose_name='Email', null=True)
    telefono = models.CharField(max_length=100, verbose_name='Telefono', null=True)
    direccion = models.CharField(max_length=100, verbose_name='Direccion', null=True)
    rubro = models.CharField(max_length=100, verbose_name='Rubro', null=True)
