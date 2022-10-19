# Generated by Django 4.1.1 on 2022-10-19 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_hostal', '0002_alter_accesorio_options_alter_cama_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accesorio',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='cama',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='cargo',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'managed': True, 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='contrato',
            options={'managed': True, 'verbose_name_plural': 'Contratos'},
        ),
        migrations.AlterModelOptions(
            name='detfactura',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'managed': True, 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelOptions(
            name='estadocontrato',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='estadohab',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='estadopedido',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='estadousuario',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='factura',
            options={'managed': True, 'verbose_name_plural': 'Facturas'},
        ),
        migrations.AlterModelOptions(
            name='familiaprod',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='habacc',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='habitacion',
            options={'managed': True, 'verbose_name_plural': 'Habitaciones'},
        ),
        migrations.AlterModelOptions(
            name='huesped',
            options={'managed': True, 'verbose_name_plural': 'Huespedes'},
        ),
        migrations.AlterModelOptions(
            name='minuta',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='ordencompra',
            options={'managed': True, 'verbose_name_plural': 'Ordenes De Compra'},
        ),
        migrations.AlterModelOptions(
            name='ordenpedido',
            options={'managed': True, 'verbose_name_plural': 'Ordenes de Pedidos'},
        ),
        migrations.AlterModelOptions(
            name='platmin',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='plato',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'managed': True, 'verbose_name_plural': 'Proveedores'},
        ),
        migrations.AlterModelOptions(
            name='servicio',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='skuproducto',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tipocama',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tipocontrato',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tipohab',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tipoplato',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tipoprod',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'managed': True},
        ),
    ]
