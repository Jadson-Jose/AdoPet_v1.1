from django.db import models

from adopter.models import Adopter
from animal.models import Animal


class Adoption(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE)
    date_of_adoption = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.animal.name} - {self.adopter.name}"
