from django.db import models

class Adopter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return self.name
