from django import forms
from admin_hostal.models import Cliente, Contrato


class ClienteForm(forms.ModelForm):   
    class Meta:
        model = Cliente
        fields = ['rut_empresa', 'nombre_empresa', 'razon_social', 'email', 'telefono','direccion',
                  'id_contrato_c','id_usuario_c']

        labels = {
            'rut_empresa': 'Rut Empresa',
            'nombre_empresa': 'Nombre Empresa',
            'razon_social': 'Razon Social',
            'email': 'Email',
            'telefono': 'Telefono',
            'direccion': 'Direccion Empresa',
            'id_contrato_c': 'Contrato',
            'id_usuario_c': 'Usuario Creador'
        }

        widgets = {
           # 'nombre': forms.TextInput(),
           # 'apellidos': forms.TextInput(),
           # 'rut_empresa': forms.TextInput(),
           # 'nombre_empresa': forms.TextInput(),
           # 'razon_social': forms.TextInput(),
           # 'email': forms.EmailInput(),
           # 'telefono': forms.TextInput(),
           # 'direccion': forms.TextInput(),
           # 'id_contrato_c': forms.ModelChoiceField(Contrato.objects.all()),
           # 'id_usuario_c': forms.TextInput()   
                    
        }
        

        