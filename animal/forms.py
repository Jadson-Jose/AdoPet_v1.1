from django import forms
from .models import Animal


class AnimalForms(forms.ModelForm):
    class Meta:
        model = Animal
        felds = ['name', 'especie', 'raca', 'age', 'porte',
                 'colour', 'description', 'photo', 'adopted', 'shelter']
        exclude = ['date_rescue']
