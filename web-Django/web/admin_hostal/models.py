from django.db import models

# Create your models here.

class Proveedor(models.Model):
    ID  = models.AutoField(primary_key=True),
    Nombre= models.CharField(max_length=100, verbose_name='Nombre'),
    Email = models.CharField(max_length=100, verbose_name='Email'),
    Telefono = models.CharField(max_length=100, verbose_name='Telefono'),
    Direccion = models.CharField(max_length=100, verbose_name='Direccion'),
    Rubro = models.CharField(max_length=100, verbose_name='Rubro')
