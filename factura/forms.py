from django import forms

from admin_hostal.models import Factura

class FacturaForm(forms.ModelForm): 
    class Meta:
        model = Factura
        fields ='__all__'