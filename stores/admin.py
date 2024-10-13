from django.contrib import admin
from .models import Logistic

# Register your models here.
@admin.register(Logistic)
class LogisticAdmin(admin.ModelAdmin):
      list_display = ('name', 'quantity', 'status', 'stocked_date', 'last_updated')
      search_fields = ('name',)
