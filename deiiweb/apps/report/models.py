from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.manager_templates.models import Template
# Create your models here.

class Report(models.Model):
    name = models.CharField(verbose_name=_('nombre'), max_length=50)
    description = models.CharField(verbose_name=_('descripción'), max_length=255)
    template = models.ForeignKey(
        Template, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name