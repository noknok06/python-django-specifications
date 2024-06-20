# specification/forms.py

from django import forms
from .models import StandardChangeMst

class StandardChangeMstForm(forms.ModelForm):
    class Meta:
        model = StandardChangeMst
        fields = ['item_id', 'change_details']
