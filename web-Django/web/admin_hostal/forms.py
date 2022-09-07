from django import forms
from .models import Cliente, Empleado, Huesped, Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields ='__all__'

class EmpleadoForm(forms.ModelForm):
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