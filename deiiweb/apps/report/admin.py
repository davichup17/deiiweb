from django.contrib import admin
from .models import Report
# Register your models here.
class ReportAdmin(admin.ModelAdmin):
    search_fields = ('name', 'content',)


admin.site.register(Report, ReportAdmin)