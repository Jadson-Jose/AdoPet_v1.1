from django import forms
from .models import Adopter


class AdopterForm(forms.ModelForm):
    class Meta:
        model = Adopter
        fields = '__all__'
