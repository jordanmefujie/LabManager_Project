from django import forms
from .models import LabTest  # Assuming LabTest is a model in your app

class LargeLabForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = [
            'test_name', 'patient_name', 'doctor_name', 'date', 
            'test_results', 'notes', 'status', 'priority', 
            'sample_type', 'equipment_used', 'lab_technician', 
            'cost', 'insurance_covered', 'comments', 'follow_up_date'
        ]
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'test_results': forms.Textarea(attrs={'rows': 4}),
            'notes': forms.Textarea(attrs={'rows': 4}),
            'comments': forms.Textarea(attrs={'rows': 4}),
        }
