from django import forms

from factura.models import Factura

class FacturaForm(forms.ModelForm): 
    class Meta:
        model = Factura
        fields ='__all__'