from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'especie', 'raca', 'age', 'porte',
                  'colour', 'description', 'photo', 'shelter']

    # Personality validation of the age

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None or age < 0 or age > 20:
            raise forms.ValidationError("A idade deve ser entre 0 e 20 anos.")
        return age

    # Validation of the name

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError(
                "O nome deve ter pelo menos 3 caracteres.")
        return name

    # validaton of the especie

    def clean_especie(self):
        especie = self.cleaned_data.get('especie')
        if especie.lower() not in ['cachorro', 'gato']:
            raise forms.ValidationError(
                "A espécie deve ser 'Cachorro' ou 'Gato'.")
        return especie

