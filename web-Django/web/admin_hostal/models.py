from django.db import models

# Create your models here.

class Proveedor(models.Model):
    id_prov  = models.AutoField(primary_key=True)
    nombre_prov = models.CharField(max_length=100, verbose_name='Nombre', null=True)
    email_prov = models.CharField(max_length=100, verbose_name='Email', null=True)
    telefono_prov = models.CharField(max_length=100, verbose_name='Telefono', null=True)
    direccion_prov = models.CharField(max_length=100, verbose_name='Direccion', null=True)
    rubro = models.CharField(max_length=100, verbose_name='Rubro', null=True)

class Empleado(models.Model):
    id_emp  = models.AutoField(primary_key=True)
    nombre_emp = models.CharField(max_length=100, verbose_name='Nombre', null=True)
    pri_apell_emp = models.CharField(max_length=100, verbose_name='Primer Apellido', null=True)
    seg_apell_emp = models.CharField(max_length=100, verbose_name='Segundo Apellido', null=True)
    email_emp = models.CharField(max_length=100, verbose_name='Email', null=True)
    telefono_emp = models.CharField(max_length=100, verbose_name='Telefono', null=True)

class Huesped(models.Model):
    id_hue  = models.AutoField(primary_key=True)
    rut_hue = models.CharField(max_length=100, verbose_name='Rut', null=True)  
    nombre_hue = models.CharField(max_length=100, verbose_name='Nombre', null=True)
    pri_apell_hue = models.CharField(max_length=100, verbose_name='Primer Apellido', null=True)
    seg_apell_hue = models.CharField(max_length=100, verbose_name='Segundo Apellido', null=True)
    email_hue = models.CharField(max_length=100, verbose_name='Email', null=True)
    telefono_hue = models.CharField(max_length=100, verbose_name='Telefono', null=True)
    direccion_prov = models.CharField(max_length=100, verbose_name='Direccion', null=True)

class Cliente(models.Model):
    id_cli = models.AutoField(primary_key=True)
    rut_cli = models.CharField(max_length=100, verbose_name='Rut', null=True)  
    nombre_cli = models.CharField(max_length=100, verbose_name='Nombre', null=True)
    razon_social = models.CharField(max_length=100, verbose_name='Razón Social', null=True)
    email_cli = models.CharField(max_length=100, verbose_name='Email', null=True)
    telefono_cli = models.CharField(max_length=100, verbose_name='Telefono', null=True)
    direccion_cli = models.CharField(max_length=100, verbose_name='Direccion', null=True)

