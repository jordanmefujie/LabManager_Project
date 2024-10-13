from django.contrib import admin
from home.models import LabTest
from home.models import LabResult

# Register your models here.
admin.site.register(LabTest)

class LabTestAdmin(admin.ModelAdmin):
    list_display = ('test_name', 'patient_name', 'doctor_name', 'date', 'status', 'priority')
    list_filter = ('status', 'priority', 'date')
    search_fields = ('test_name', 'patient_name', 'doctor_name')
    ordering = ('-date',)  # Order by date descending

class LabResultInline(admin.TabularInline):
    model = LabResult
    extra = 1  # Number of extra empty fields to show

class LabTestAdmin(admin.ModelAdmin):
    inlines = [LabResultInline]

def mark_as_completed(modeladmin, request, queryset):
    queryset.update(status='completed')
mark_as_completed.short_description = "Mark selected tests as completed"

class LabTestAdmin(admin.ModelAdmin):
    actions = [mark_as_completed]

class LabTestAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Test Information', {
            'fields': ('test_name', 'date', 'status', 'priority')
        }),
        ('Patient Details', {
            'fields': ('patient_name', 'doctor_name', 'lab_technician')
        }),
        ('Results', {
            'fields': ('test_results', 'notes', 'comments')
        }),
    )

class LabTestAdmin(admin.ModelAdmin):
    readonly_fields = ('date', 'lab_technician')

class LabTestAdmin(admin.ModelAdmin):
    prepopulated_fields = {'test_slug': ('test_name',)}
