from django.test import TestCase
from django.contrib.auth.models import User
from .models import Report

# Create your tests here.
class ReportModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='password')
        self.report = Report.objects.create(
                title='Sample Report',
                content='This is a test report content.',
                author=user
                )

    def test_report_creation(self):
        self.assertEqual(self.report.title, 'Sample Report')
        self.assertEqual(self.report.content, 'This is a test report content.')
