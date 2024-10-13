from django.db import models
from django.contrib.auth.models import User

# Equipment Model
class Equipment(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('In Use', 'In Use'),
        ('Maintenance', 'Maintenance'),
        ('Decommissioned', 'Decommissioned'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    purchase_date = models.DateField()
    last_maintenance = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    maintenance_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Experiment Model
class Experiment(models.Model):
    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    equipment = models.ManyToManyField(Equipment)
    researchers = models.ManyToManyField(User)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Planned')

    def __str__(self):
        return self.title


# Lab Test Model
class LabTest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    test_date = models.DateField()

    def __str__(self):
        return self.name


# Lab Test Request Model
class LabTestRequest(models.Model):
    TEST_CHOICES = [
        ('HB', 'HB'),
        ('WBC', 'WBC'),
        ('PLT', 'PLT'),
        ('RBC', 'RBC'),
        ('BF', 'BF'),
        ('WIDAL', 'WIDAL'),
        ('BLOOD GROUP', 'BLOOD GROUP'),
        ('URINE R/E', 'URINE R/E'),
        ('STOOL R/E', 'STOOL R/E'),
        ('HIV', 'HIV'),
        ('VDRL', 'VDRL'),
        ('SICKLING TEST', 'SICKLING TEST'),
        ('LFT', 'LFT'),
        ('RFT', 'RFT'),
        ('FBS/RBS', 'FBS/RBS'),
        ('HBsAg', 'HBsAg'),
    ]

    test_name = models.CharField(max_length=50, choices=TEST_CHOICES, blank=True)
    custom_test_name = models.CharField(max_length=255, blank=True, help_text="Enter a custom test name if needed.")
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Verified', 'Verified')], default='Pending')

    def __str__(self):
        return f"{self.get_test_display() or self.custom_test_name} requested by {self.requested_by}"


# Lab Report Model
class LabReport(models.Model):
    lab_test = models.OneToOneField(LabTest, on_delete=models.CASCADE, related_name='report')
    report_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    test_request = models.ForeignKey(LabTestRequest, on_delete=models.CASCADE)
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.lab_test.name}"


# Lab Result Verification Model
class LabResultVerification(models.Model):
    lab_test = models.OneToOneField(LabTest, on_delete=models.CASCADE, related_name='verification')
    verified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    verified_at = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()

    def __str__(self):
        return f"Verification for {self.lab_test.name}"
