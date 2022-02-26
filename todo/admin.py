from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'create', 'user_id')