from django.db import models

from shelter.models import Shelter


# TODO Melhorar o TextChoices para uma maior organização e legibilidade da Model

class Animal (models.Model):
    
    PORTE_CHOICES = [
        ('P', 'Pequeno'),
        ('M', 'Medio'),
        ('G', 'Grande'),
    ]
    
    
    
    name = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)  # Exemplo: Cachorro, Gato
    raca = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField()  # Em anos
    porte = models.CharField(max_length=1, choices=PORTE_CHOICES)  # Exemplo: Pequeno, Médio, Grande
    colour = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='animal_photos/', blank=True, null=True)
    date_rescue = models.DateField(auto_now_add=True)
    adopted = models.BooleanField(default=False)

    # Animal Shelter Relationship
    shelter = models.ForeignKey(
        Shelter, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
