from django import forms
from admin_hostal.models import Huesped


class HuespedForm(forms.ModelForm):
    class Meta:
        model = Huesped
        fields ='__all__'

