from django.forms import ModelForm
from django import forms
from .models import Student



class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['old_bus', 'area','adress']
