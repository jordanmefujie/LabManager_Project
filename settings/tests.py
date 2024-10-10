from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserPreference, AppConfig

# Create your tests here.
class UserPreferenceModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='password')
        self.pref = UserPreference.objects.create(
                user=user,
                preference_name='theme',
                preference_value='dark'
                )

    def test_user_preference_creation(self):
        self.assertEqual(self.pref.preference_name, 'theme')
        self.assertEqual(self.pref.preference_value, 'dark')

class AppConfigModelTest(TestCase):
    def setUp(self):
        self.config = AppConfig.objects.create(
                config_name='site_title',
                config_value='LabManager'
                )

    def test_app_config_creation(self):
        self.assertEqual(self.config.config_name, 'site_title')
        self.assertEqual(self.config.config_value, 'LabManager')
