from django import forms
from .models import Animal


class AnimalForms(forms.ModelForm):
    class Meta:
        model = Animal
        felds = '__all__'
