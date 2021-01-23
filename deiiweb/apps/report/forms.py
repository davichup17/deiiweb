from django import forms
from .models import Report
from apps.manager_templates.models import Template

class ReportForm(forms.ModelForm):
    plantillas = Template.objects.all()
    class Meta:
        model = Report
        fields = ('name', 'description')
    template = forms.ChoiceField(choices=plantillas, required=True, label="Seleccione la plantilla")  