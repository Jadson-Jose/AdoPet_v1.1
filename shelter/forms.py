from django import forms
from .models import Shelter


class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = felds = ['name', 'city', 'state', 'address', 'number',
                 'cep', 'phone', 'email', 'photo']
