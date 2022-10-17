from django import forms
from admin_hostal.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields ='__all__'

