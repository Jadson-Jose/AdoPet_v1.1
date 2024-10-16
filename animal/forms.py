from django import forms
from .models import Animal


class AnimalForms(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'especie', 'raca', 'age', 'porte',
                  'colour', 'description', 'photo', 'shelter']
