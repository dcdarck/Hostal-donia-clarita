from django import forms
from django.forms import ValidationError
from admin_hostal.models import Proveedor

class ProveedorForm(forms.ModelForm): 
    nombre_prov = forms.CharField(label= "Nombre proveedor", min_length=3, max_length=35)
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