from django import forms
from .models import Template


class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título', 'label':''}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }
