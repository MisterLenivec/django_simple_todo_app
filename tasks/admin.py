from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'complete', 'created', 'updated']


admin.site.register(Task, TaskAdmin)
