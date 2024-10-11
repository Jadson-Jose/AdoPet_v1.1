from django import forms
from .models import Adopter


class AdopterForm(forms.ModelForm):
    class Meta:
        model = Adopter
        fields = ['name', 'email', 'phone', 'address', 'number', 'complement',
                  'neighborhood', 'city', 'state', 'cep', 'date_of_birth']
