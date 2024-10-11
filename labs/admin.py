from django.contrib import admin
from .models import Lab

# Register your models here.
@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact_number', 'email')
    search_fields = ('name', 'location')
