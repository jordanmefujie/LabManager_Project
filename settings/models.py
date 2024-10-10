from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preference_name = models.CharField(max_length=100)
    preference_value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} - {self.preference_name}'

class AppConfig(models.Model):
    config_name = models.CharField(max_length=100, unique=True)
    config_value = models.CharField(max_length=255)

    def __str__(self):
        return self.config_name
