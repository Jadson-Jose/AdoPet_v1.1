from django.contrib import admin
from .models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'especie', 'raca', 'age', 'porte', 'adopted')
    list_filter = ('especie', 'porte', 'adopted')
    search_fields = ('name', 'raca')
