from django.db import models
from django.core.validators import RegexValidator


class Adopter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, validators=[RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="O número de telefone deve estar no formato: '+999999999'. Máximo de 15 dígitos.")])
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=[(
        'SP', 'São Paulo'), ('RJ', 'Rio de Janeiro'), ('MG', 'Minas Gerais')])
    cep = models.CharField(max_length=8, validators=[RegexValidator(
        regex=r'^\d{8}$', message="O CEP deve ter 8 dígitos.")])
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return self.name
