from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control',
            'id':'first_name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control',
            'id':'last_name'}),
            'age':forms.TextInput(attrs={'class':'form-control',
            'id':'age'}),
            'city':forms.TextInput(attrs={'class':'form-control',
            'id':'city'}),
            'address':forms.TextInput(attrs={'class':'form-control',
            'id':'address'}),
        }
        
