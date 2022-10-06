from django.db import models
from bases.models import ClaseModelo
# Create your models here.

class Cliente(ClaseModelo):
    id_cliente = models.AutoField(primary_key=True)
    rut_empresa = models.CharField(max_length=45, help_text='Rut de Empresa', unique=True)
    nombre_empresa = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=45)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.nombre_empresa)

    def guardar(self):
        self.nombre_empresa = self.nombre_empresa.upper()

        super(Cliente, self).guardar()

    class Meta:
        verbose_name_plural = "Clientes"
        db_table = 'CLIENTE'

