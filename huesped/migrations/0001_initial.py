# Generated by Django 4.1.1 on 2022-10-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Huesped',
            fields=[
                ('id_huesped', models.AutoField(primary_key=True, serialize=False)),
                ('rut_huesped', models.CharField(max_length=45)),
                ('nombre', models.CharField(max_length=100)),
                ('p_apellido', models.CharField(max_length=100)),
                ('s_apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Empleados',
                'db_table': 'HUESPED',
            },
        ),
    ]
