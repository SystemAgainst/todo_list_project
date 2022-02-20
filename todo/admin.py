from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_data',)

admin.site.register(Todo, TodoAdmin)