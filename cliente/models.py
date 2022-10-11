from pyexpat import model
from django.db import models
# Create your models here.

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut_empresa = models.CharField(max_length=45, help_text='Rut de Empresa', unique=True)
    nombre_empresa = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=200)    

    class Meta:
        verbose_name_plural = "Clientes"
        db_table = 'CLIENTE'

