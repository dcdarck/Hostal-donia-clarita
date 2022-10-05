from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields ='__all__'
        #fields = ['descripcion', 'estado']
        #labels = {'descripcion': "Descripción de la categoría", "estado": "Estado"}
        #widget = {'descripcion': forms.TextInput}

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    for field in iter(self.fields):
    #        self.fields[field].widget.attrs.update({'class': 'form-control'})