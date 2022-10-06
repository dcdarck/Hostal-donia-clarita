from django.db import models
from bases.models import ClaseModelo2

class Empleado(ClaseModelo2):
    id_empleado = models.AutoField(primary_key=True)
    rut_empleado = models.CharField(max_length=45)
    nombre_empleado = models.CharField(max_length=45)
    p_apellido = models.CharField(max_length=45)
    s_apellido = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45)
    fono = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'EMPLEADO'