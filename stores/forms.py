# stores/forms.py
from django import forms
from .models import Commodity

class CommodityForm(forms.ModelForm):
    class Meta:
        model = Commodity
        fields = ['name', 'category', 'quantity', 'supplier', 'stocking_date']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError('Quantity must be a positive number.')
        return quantity

    def clean_stocking_date(self):
        stocking_date = self.cleaned_data.get('stocking_date')
        if stocking_date > timezone.now().date():
            raise forms.ValidationError('Stocking date cannot be in the future.')
        return stocking_date

class AddCommodityForm(forms.ModelForm):
    class Meta:
        model = Commodity
        fields = ['name', 'category', 'quantity', 'supplier', 'stocking_date']

class UpdateLogisticsForm(forms.ModelForm):
    class Meta:
        model = Commodity  # Specify the model linked to this form
        fields = ['name', 'category', 'quantity', 'supplier', 'stocking_date']  # Adjust fields based on your model
