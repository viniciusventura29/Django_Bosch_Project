from dataclasses import fields
from typing import Text
from django import forms
from home.models import TextModel, UsuarioModel

class TextoModelForm(forms.ModelForm):
    
    class Meta:
        model = TextModel
        
        fields = '__all__'
        
class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = UsuarioModel
        
        fields = '__all__'