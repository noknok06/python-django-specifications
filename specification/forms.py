# forms.py

from django import forms
from .models import StandardChangeMst

class DateInput(forms.DateInput):
    input_type = 'date'

class Textnput(forms.TextInput):
    input_type = 'text'
    
class StandardChangeMstForm(forms.ModelForm):
    class Meta:
        model = StandardChangeMst
        fields = ['update_date', 'item_id', 'change_details', 'attachment']
        widgets = {
            'item_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Item ID'}),
            'update_date': DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'change_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter Change Details'}),
            'attachment': forms.FileInput(attrs={'class': 'form-control-file'})
        }
