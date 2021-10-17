from django.contrib import admin

# Register your models here.
from movies.models import *


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'director', 'description']
    list_editable = ['director', 'description']
    search_fields = ['name', 'director', 'description']
