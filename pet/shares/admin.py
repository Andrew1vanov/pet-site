from django.contrib import admin
from .models import Security

# Register your models here.

@admin.register(Security)
class SecurityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'short_name', 'sec_id', 'board', 'description']
    prepopulated_fields = {'slug':('name',)}