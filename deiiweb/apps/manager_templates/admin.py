from django.contrib import admin
from .models import Template

# Register your models here.
class TemplateAdmin(admin.ModelAdmin):
    search_fields = ('name', 'content',)


admin.site.register(Template, TemplateAdmin)