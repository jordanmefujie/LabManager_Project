from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
