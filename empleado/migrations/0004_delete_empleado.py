# Generated by Django 4.1.1 on 2022-10-16 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0003_alter_empleado_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empleado',
        ),
    ]