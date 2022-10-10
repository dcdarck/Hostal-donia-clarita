from django.db import models
from bases.models import ClaseModelo2

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_prov = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)    
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=80)
    rubro = models.CharField(max_length=25, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Proveedores'
        db_table = 'PROVEEDOR'  
        