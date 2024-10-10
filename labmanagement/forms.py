from django import forms
from .models import Equipment, Experiment, LabTestRequest, LabReport, LabResultVerification, LabTest

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'category', 'maintenance_date', 'is_available']


class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['title', 'description', 'status']


class LabTestRequestForm(forms.ModelForm):
    class Meta:
        model = LabTestRequest
        fields = ['test_name', 'custom_test_name', 'requested_by', 'patient_name', 'status']

    def clean(self):
        cleaned_data = super().clean()
        test_name = cleaned_data.get('test_name')
        custom_test_name = cleaned_data.get('custom_test_name')

        if not test_name and not custom_test_name:
            raise forms.ValidationError('You must select a test or enter a custom test name.')

        return cleaned_data


class LabReportForm(forms.ModelForm):
    class Meta:
        model = LabReport
        fields = ['report_content']


class LabResultVerificationForm(forms.ModelForm):
    class Meta:
        model = LabResultVerification
        fields = ['comments']

class LabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ['test_date', 'description', 'name']
