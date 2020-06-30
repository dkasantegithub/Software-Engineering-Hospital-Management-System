from django import forms
from .models import Patient_Record
from django.contrib.admin import widgets

CHOICES = [ 
    ('M','Male'), 
    ('F', 'Female'), 
    ]

class DateInput(forms.DateInput):
    input_type = 'date'

    
class RegisterForm(forms.Form):
    first_name = forms.CharField(
                widget=forms.TextInput(attrs={'class':'form-control'}), 
                required=True
                )
    last_name = forms.CharField(
                widget=forms.TextInput(attrs={'class':'form-control'}), 
                required=True
                )
    gender = forms.ChoiceField(
                widget=forms.RadioSelect, choices=CHOICES, 
                required=True
                )
    contact = forms.CharField(
                widget=forms.NumberInput(attrs={'class':'form-control'}), 
                required=True
                )
    residential_address = forms.CharField(
                widget=forms.TextInput(attrs={'class':'form-control'}), 
                required=True
                )
    date_of_birth = forms.DateField(
                widget=DateInput(attrs={'class':'form-control'}), 
                required=True
                )


class PatientLogForm(forms.ModelForm):
    class Meta:
        model = Patient_Record
        fields = '__all__'
        widgets = {
            'check_in_date': DateInput(attrs={'class':'form-control'}),
            'check_in_period': forms.Select(attrs={'class':'form-control'}),
            'check_out_date': DateInput(attrs={'class':'form-control'}),
            'check_out_period': forms.Select(attrs={'class': 'form-control'}),
            'patient': forms.Select(attrs={'class':'form-control'}),
            'assigned_doctor': forms.Select(attrs={'class': 'form-control'}),
        }
