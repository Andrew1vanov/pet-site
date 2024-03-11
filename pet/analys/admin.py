from django.contrib import admin
from .models import MovingAverages

# Register your models here.
@admin.register(MovingAverages)
class MovingAdmin(admin.ModelAdmin):
    list_display = ['name', 'period', 'linestyle', 'color', 'lineType']
