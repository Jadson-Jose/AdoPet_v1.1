from django.contrib import admin
from .models import Adopter


@admin.register(Adopter)
class AdopterAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'city', 'state']
    search_fields = ['name', 'email']
    list_filter = ['state']
