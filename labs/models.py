from django.db import models
from django.utils import timezone

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

class LabTechnician(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    model_number = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=100)
    last_maintenance_date = models.DateField()

    def __str__(self):
        return self.name

class LabTest(models.Model):
    TEST_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    test_name = models.CharField(max_length=200)
    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    test_results = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=TEST_STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    sample_type = models.CharField(max_length=50)  # e.g., Blood, Urine, etc.
    equipment_used = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    lab_technician = models.ForeignKey(LabTechnician, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    insurance_covered = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    follow_up_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.test_name} for {self.patient_name}"

    class Meta:
        ordering = ['date']
