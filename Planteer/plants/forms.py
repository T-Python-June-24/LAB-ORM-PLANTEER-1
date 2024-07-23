from django import forms
from plants.models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model=Plant
        fields="__all__"
        # or fields=["name","....",..]
        widgets={
            'name': forms.TextInput({"class":"form-control"})
        }