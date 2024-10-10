from django.test import TestCase
from django.contrib.auth.models import User
from .models import Equipment, Experiment

# Create your tests here.
class EquipmentModelTest(TestCase):
    def setUp(self):
        self.equipment = Equipment.objects.create(
        name='Microscope',
        category='Optical',
        description='A high-resolution microscope',
        purchase_date='2023-01-15',
        status='Available'
        )

    def test_equipment_creation(self):
        self.assertEqual(self.equipment.name, 'Microscope')

class ExperimentModelTest(TestCase):
    def setUp(self):
        self.experiment = Experiment.objects.create(
                title='DNA Sequencing',
                description='Sequencing DNA samples',
                start_date='2023-08-01',
                status='Planned'
                )

    def test_experiment_creation(self):
        self.assertEqual(self.experiment.title, 'DNA Sequencing')
