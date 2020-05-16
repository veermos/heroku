from django.forms import ModelForm
from django import forms
from .models import Fees

class DateInput(forms.DateInput):
    input_type = 'date'

class FeesForm(ModelForm):
    class Meta:
        model = Fees
        fields = ['kind', 'payment_date', 'bank_account','value']
    payment_date = forms.DateField(widget=DateInput)
