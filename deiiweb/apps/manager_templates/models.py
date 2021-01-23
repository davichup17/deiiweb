from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from django.conf import settings
import io
import os
import shutil

# Create your models here.

class Template(models.Model):
    name = models.CharField(verbose_name=_('nombre'), max_length=50)
    content = RichTextField(verbose_name="Contenido", blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        fname = settings.MEDIA_ROOT + '/templates/' + self.name + '.html'
        if os.path.isfile(fname):
            fnamebk = settings.MEDIA_ROOT + '/templates/' + self.name + 'bk.html'
            shutil.move(fname, fnamebk)
        with open(fname, 'w') as destination:
            content = self.content.split('\n')
            for line in content:
                destination.write(line)
            destination.close()
        super().save(*args, **kwargs)

