from dataclasses import fields
from typing import Text
from django import forms
from home.models import TextModel

class TextoModelForm(forms.ModelForm):
    
    class Meta:
        model = TextModel
        
        fields = '__all__'