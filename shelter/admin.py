from django.contrib import admin
from .models import Shelter


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'phone']
    search_fields = ['name', 'city']
    list_filter = ['state',]
