# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accesorio(models.Model):
    id_accesorio = models.IntegerField(primary_key=True)
    accesorio = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ACCESORIO'


class Cama(models.Model):
    id_cama = models.IntegerField(primary_key=True)
    cant_cojines = models.IntegerField()
    id_tipo_cama_c = models.ForeignKey('TipoCama', models.DO_NOTHING, db_column='id_tipo_cama_c')

    class Meta:
        managed = False
        db_table = 'CAMA'
        unique_together = (('id_cama', 'id_tipo_cama_c'),)


class Cargo(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    cargo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'CARGO'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut_empresa = models.CharField(max_length=45)
    nombre_empresa = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=45)
    direccion = models.CharField(max_length=200)
    id_usuario_c = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario_c', blank=True, null=True)
    id_contrato_c = models.ForeignKey('Contrato', models.DO_NOTHING, db_column='id_contrato_c', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CLIENTE'


class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    fecha_ini = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    cant_huesp = models.IntegerField()
    id_estado_contrato_c = models.ForeignKey('EstadoContrato', models.DO_NOTHING, db_column='id_estado_contrato_c', blank=True, null=True)
    id_tipo_contrato_c = models.ForeignKey('TipoContrato', models.DO_NOTHING, db_column='id_tipo_contrato_c', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CONTRATO'


class DetFactura(models.Model):
    id_det_factura = models.AutoField(primary_key=True)
    monto_t = models.IntegerField()
    sub_total = models.IntegerField()
    iva = models.IntegerField()
    id_factura_d = models.ForeignKey('Factura', models.DO_NOTHING, db_column='id_factura_d', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DET_FACTURA'


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    rut_empleado = models.CharField(max_length=45)
    nombre_empleado = models.CharField(max_length=45)
    p_apellido = models.CharField(max_length=45)
    s_apellido = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45)
    fono = models.CharField(max_length=45)
    id_usuario_e = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario_e', blank=True, null=True)
    id_cargo_e = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo_e')

    class Meta:
        managed = False
        db_table = 'EMPLEADO'
        unique_together = (('id_empleado', 'id_cargo_e'),)


class EstadoContrato(models.Model):
    id_estado_contrato = models.IntegerField(primary_key=True)
    estado_contrato = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ESTADO_CONTRATO'


class EstadoHab(models.Model):
    id_estado_hab = models.IntegerField(primary_key=True)
    estado_hab = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ESTADO_HAB'


class EstadoPedido(models.Model):
    id_estado_p = models.IntegerField(primary_key=True)
    estado_pedido = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ESTADO_PEDIDO'


class EstadoUsuario(models.Model):
    id_estado_user = models.IntegerField(primary_key=True)
    estado_user = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ESTADO_USUARIO'


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    fecha = models.DateField()
    nombre_empresa = models.CharField(max_length=100)
    subtotal = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()
    id_cliente = models.IntegerField()
    num_orden_f = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='num_orden_f', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FACTURA'


class FamiliaProd(models.Model):
    id_familia_p = models.IntegerField(primary_key=True)
    familia_p = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'FAMILIA_PROD'


class Habitacion(models.Model):
    num_habitacion = models.AutoField(primary_key=True)
    precio = models.IntegerField()
    id_estado_hab_h = models.ForeignKey(EstadoHab, models.DO_NOTHING, db_column='id_estado_hab_h', blank=True, null=True)
    id_tipo_hab_h = models.ForeignKey('TipoHab', models.DO_NOTHING, db_column='id_tipo_hab_h')
    id_tipo_cama_h = models.ForeignKey('TipoCama', models.DO_NOTHING, db_column='id_tipo_cama_h', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HABITACION'
        unique_together = (('num_habitacion', 'id_tipo_hab_h'),)


class HabAcc(models.Model):
    id_hab_acc = models.IntegerField(primary_key=True)
    id_acc_ha = models.ForeignKey(Accesorio, models.DO_NOTHING, db_column='id_acc_ha', blank=True, null=True)
    id_hab_ha = models.ForeignKey(Habitacion, models.DO_NOTHING, db_column='id_hab_ha', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HAB_ACC'


class Huesped(models.Model):
    id_huesped = models.AutoField(primary_key=True)
    rut_huesped = models.CharField(max_length=45)
    nombre = models.CharField(max_length=100)
    p_apellido = models.CharField(max_length=100)
    s_apellido = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=45)
    id_cliente_h = models.IntegerField()
    num_orden_h = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='num_orden_h', blank=True, null=True)
    num_habitacion_h = models.ForeignKey(Habitacion, models.DO_NOTHING, db_column='num_habitacion_h', blank=True, null=True)
    id_minuta_h = models.ForeignKey('Minuta', models.DO_NOTHING, db_column='id_minuta_h', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUESPED'


class Minuta(models.Model):
    id_minuta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'MINUTA'


class OrdenCompra(models.Model):
    num_orden = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    id_huesped = models.IntegerField()
    nombre_huesped = models.CharField(max_length=200)
    id_factura = models.IntegerField()
    id_cliente_o = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente_o', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ORDEN_COMPRA'


class OrdenPedido(models.Model):
    num_pedido = models.AutoField(primary_key=True)
    fecha_pedido = models.DateField()
    fecha_llegada = models.DateField(blank=True, null=True)
    id_proveedor_o = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor_o', blank=True, null=True)
    id_estado_p_o = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='id_estado_p_o', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ORDEN_PEDIDO'


class Plato(models.Model):
    id_plato = models.AutoField(primary_key=True)
    nombre_plato = models.CharField(max_length=45)
    id_tipo_plato_p = models.ForeignKey('TipoPlato', models.DO_NOTHING, db_column='id_tipo_plato_p')
    id_producto_p = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto_p', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PLATO'
        unique_together = (('id_plato', 'id_tipo_plato_p'),)


class PlatMin(models.Model):
    id_plat_min = models.IntegerField(primary_key=True)
    id_plat_pm = models.ForeignKey(Plato, models.DO_NOTHING, db_column='id_plat_pm', blank=True, null=True)
    id_min_pm = models.ForeignKey(Minuta, models.DO_NOTHING, db_column='id_min_pm', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PLAT_MIN'


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    fecha_venc = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    stock_critico = models.IntegerField()
    id_sku_p = models.ForeignKey('SkuProducto', models.DO_NOTHING, db_column='id_sku_p', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PRODUCTO'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_prov = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=45)
    direccion = models.CharField(max_length=200)
    rubro = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PROVEEDOR'


class Servicio(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    servicio = models.CharField(max_length=100)
    id_factura_s = models.ForeignKey(Factura, models.DO_NOTHING, db_column='id_factura_s', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SERVICIO'


class SkuProducto(models.Model):
    id_sku = models.AutoField(primary_key=True)
    sku = models.IntegerField(db_column='SKU')  # Field name made lowercase.
    fecha_venc = models.IntegerField()
    id_proveedor_s = models.ForeignKey(OrdenPedido, models.DO_NOTHING, db_column='id_proveedor_s', to_field='id_proveedor_o', blank=True, null=True)
    id_familia_s = models.ForeignKey(FamiliaProd, models.DO_NOTHING, db_column='id_familia_s', blank=True, null=True)
    id_tipo_producto_s = models.ForeignKey('TipoProd', models.DO_NOTHING, db_column='id_tipo_producto_s', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SKU_PRODUCTO'


class TipoCama(models.Model):
    id_tipo_cama = models.IntegerField(primary_key=True)
    tipo_cama = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'TIPO_CAMA'


class TipoContrato(models.Model):
    id_tipo_contrato = models.IntegerField(primary_key=True)
    tipo_contrato = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'TIPO_CONTRATO'


class TipoHab(models.Model):
    id_tipo_hab = models.IntegerField(primary_key=True)
    tipo_hab = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'TIPO_HAB'


class TipoPlato(models.Model):
    id_tipo_plato = models.IntegerField(primary_key=True)
    tipo_plato = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'TIPO_PLATO'


class TipoProd(models.Model):
    id_tipo_prod = models.IntegerField(primary_key=True)
    tipo_prod = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'TIPO_PROD'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=45)
    tipo_usuario = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    pwd = models.CharField(max_length=45)
    id_estado_u = models.ForeignKey(EstadoUsuario, models.DO_NOTHING, db_column='id_estado_u', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'USUARIO'
