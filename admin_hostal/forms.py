#Código creado por Agustín llaña, Matías Quidel, Jesús Reyes
import email
from django import forms
from .models import Cliente, Empleado, Huesped, Proveedor
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.utils.translation import gettext_lazy as _

class ProveedorForm(forms.ModelForm): 
    nombre_prov = forms.CharField(min_length=3, max_length=35)
    email = forms.EmailField(min_length=3, max_length=100)
    telefono = forms.IntegerField() 
    direccion = forms.CharField(min_length=3, max_length=75)
    rubro = forms.CharField(min_length=3, max_length=35, required=False)
    
   #validador objetos repetidos 
    def clean_nombre_prov(self):
        nombre_prov = self.cleaned_data["nombre_prov"]
        existe = Proveedor.objects.filter(nombre_prov__iexact=nombre_prov).exists()            
        if existe:
                raise ValidationError("Este proveedor ya existe")            
        return nombre_prov

    class Meta:
        model = Proveedor
        fields ='__all__'
        
    #formulario para editar(sin objetos repetidos) 
class ProveedorEdit(forms.ModelForm):
    nombre_prov = forms.CharField(min_length=3, max_length=35)
    email = forms.EmailField(min_length=3, max_length=100)
    telefono = forms.IntegerField() 
    direccion = forms.CharField(min_length=3, max_length=75)
    rubro = forms.CharField(min_length=3, max_length=35, required=False)
    
    class Meta:
        model = Proveedor
        fields ='__all__'
        
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
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields ='__all__'

class HuespedForm(forms.ModelForm):
    class Meta:
        model = Huesped
        fields ='__all__'
