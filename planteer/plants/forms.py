from django import forms
from .models import Plant, Contact

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'about', 'used_for', 'image', 'category', 'is_edible']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Plant Name'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'About the Plant'}),
            'used_for': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Used For'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'is_edible': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
