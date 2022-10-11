from django.db import models

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    fecha = models.DateField()
    nombre_empresa = models.CharField(max_length=100)
    subtotal = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        verbose_name_plural = "Facturas"
        db_table = 'FACTURA'