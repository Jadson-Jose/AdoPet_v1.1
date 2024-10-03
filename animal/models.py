from django.db import models

from shelter.models import Shelter


class Animal (models.Model):

    TYPES = [
        ('C', 'Cachorro'),
        ('G', 'Gato'),
        ('P', 'Pássaro'),
        ('R', 'Roedor'),
        ('O', 'Outros'),
    ]

    PORTES = [
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    ]

    name = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)  # Exemplo: Cachorro, Gato
    raca = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField()  # Em anos
    porte = models.CharField(max_length=20)  # Exemplo: Pequeno, Médio, Grande
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
