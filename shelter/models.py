from django.db import models
from django.core.validators import RegexValidator

class Shelter(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, default='cidade desconhecida', choices=[(
        'SP', 'São Paulo'), ('RJ', 'Rio de Janeiro'), ('MG', 'Minas Gerais')]) 
    address = models.CharField(max_length=255)
    cep = models.CharField(max_length=8, validators=[RegexValidator(
        regex=r'^\d{8}$', message="O CEP deve ter 8 dígitos.")])
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    photo = models.ImageField(
        upload_to='shelter_photos/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name
