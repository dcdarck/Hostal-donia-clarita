from django import forms
from django.forms import ValidationError
from admin_hostal.models import Empleado

class EmpleadoForm(forms.ModelForm):
    rut_empleado = forms.CharField(min_length=8, max_length=13)
    nombre_empleado = forms.CharField(min_length=3, max_length=35)
    p_apellido = forms.CharField(min_length=3, max_length=35)
    s_apellido= forms.CharField(min_length=3, max_length=35)
    email = forms.EmailField(min_length=3, max_length=100)
    fono = forms.IntegerField()

    def clean_rut_empleado(self):
        rut_empleado = self.cleaned_data["rut_empleado"]
        existe = Empleado.objects.filter(rut_empleado__iexact=rut_empleado).exists()
        if existe:
                raise ValidationError("Este empleado ya existe")            
        return rut_empleado
     
    class Meta:
        model = Empleado
        fields ='__all__'

class EmpleadoEdit(forms.ModelForm):
    rut_empleado = forms.CharField(min_length=8, max_length=13)
    nombre_empleado = forms.CharField(min_length=3, max_length=35)
    p_apellido = forms.CharField(min_length=3, max_length=35)
    s_apellido= forms.CharField(min_length=3, max_length=35)
    email = forms.EmailField(min_length=3, max_length=100)
    fono = forms.IntegerField()
    
    class Meta:
        model = Empleado
        fields ='__all__'