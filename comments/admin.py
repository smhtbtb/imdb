from django.contrib import admin

# Register your models here.
from comments.models import *


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['passage', 'rating', 'user', 'movie']
    search_fields = ['passage', 'rating', 'user', 'movie']
