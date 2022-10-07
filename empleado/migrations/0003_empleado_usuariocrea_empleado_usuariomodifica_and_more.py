# Generated by Django 4.1.1 on 2022-10-07 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empleado', '0002_alter_empleado_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='usuarioCrea',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='empleado',
            name='usuarioModifica',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='rut_empleado',
            field=models.CharField(help_text='Rut de Empleado', max_length=45, unique=True),
        ),
    ]
