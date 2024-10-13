from django.db import models

# Create your models here.
class LabTest(models.Model):
    test_name = models.CharField(max_length=255)
    patient_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)

    def __str__(self):
        return self.test_name

class LabResult(models.Model):
    lab_test = models.ForeignKey('LabTest', on_delete=models.CASCADE)
    result_value = models.CharField(max_length=255)
    result_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.lab_test.test_name}: {self.result_value}"
