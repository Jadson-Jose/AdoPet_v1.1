from django.contrib import admin
from .models import Adoption


@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    list_display = ['animal', 'adopter', 'date_of_adoption']
    search_fields = ['animal__name', 'adopter__name']
    list_filter = ['date_of_adoption']
