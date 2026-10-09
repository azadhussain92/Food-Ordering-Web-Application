from django import forms
from.models import FoodItems


class MenuForm(forms.ModelForm):

    class Meta:
        model = FoodItems
        fields = [
            'name',
            'price',
            'image',
            'Categery',
            'is_available'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'Categery': forms.Select(attrs={'class': 'form-select'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }