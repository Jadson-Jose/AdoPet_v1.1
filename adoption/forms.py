from django import forms
from .models import Adoption


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = '__all__'
