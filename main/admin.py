from django.contrib import admin
from .models import HomeImageModel


@admin.register(admin.ModelAdmin)
class HomeImageModelAdmin(HomeImageModel):
    list_display = ['name']
    list_display_links = ['name']