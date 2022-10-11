from django.db import models
# Create your models here.

class Huesped(models.Model):
    id_huesped = models.AutoField(primary_key=True)
    rut_huesped = models.CharField(max_length=45)
    nombre = models.CharField(max_length=100)
    p_apellido = models.CharField(max_length=100)
    s_apellido = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Huespedes'
        db_table = 'HUESPED'
