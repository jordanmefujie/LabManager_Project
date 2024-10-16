from django.contrib import admin
from .models import UserPreference, AppConfig

# Register your models here.
@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'preference_name', 'preference_value')
    search_fields = ('user__username', 'preference_name')

@admin.register(AppConfig)
class AppConfigAdmin(admin.ModelAdmin):
    list_display = ('config_name', 'config_value')
    search_fields = ('config_name',)
