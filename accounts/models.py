from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Profile model linked to User
class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='customer')
    organization = models.CharField(max_length=255, blank=True)  # e.g., Lab name or organization
    
    def __str__(self):
        return f"{self.user.username} ({self.get_user_type_display()})"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
   # role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('LabManager', 'Lab Manager')])
   # role = models.CharField(max_length=50, default='default_role')
    role = models.CharField(
    max_length=50, 
    choices=[('Admin', 'Admin'), ('LabManager', 'Lab Manager')],
    default='LabManager'  # Provide a default value here
) 
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)  # Corrected field name

    def __str__(self):
        return self.user.username
