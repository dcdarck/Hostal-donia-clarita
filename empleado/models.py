from django.db import models
from bases.models import ClaseModelo2

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    rut_empleado = models.CharField(max_length=45, help_text='Rut de Empleado', unique=True)
    nombre_empleado = models.CharField(max_length=45)
    p_apellido = models.CharField(max_length=45)
    s_apellido = models.CharField(max_length=45, blank=True, null=True)
    email = models.EmailField(max_length=45)
    fono = models.IntegerField()

    class Meta:
        verbose_name_plural = "Empleado"
        db_table = 'EMPLEADO'