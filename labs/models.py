from django.db import models

# Create your models here.
class Lab(models.Model):
    name = models.CharField(max_length=255)  # Lab name
    location = models.CharField(max_length=255)  # Lab location (city, state, etc.)
    contact_number = models.CharField(max_length=15, blank=True, null=True)  # Optional contact number
    email = models.EmailField(blank=True, null=True)  # Optional email address
    description = models.TextField(blank=True, null=True)  # Optional description of the lab
    services_offered = models.TextField(blank=True, null=True)  # List of services offered by the lab
    website = models.URLField(blank=True, null=True)  # Optional website URL

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Laboratory"
        verbose_name_plural = "Laboratories"
        ordering = ['name']
