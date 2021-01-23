from django.urls import path
from .views import *

reports_patterns = ([
    path('', ReportListView.as_view(), name="reports"),
    path('create/', ReportCreateView.as_view(), name="create"),
    path('update/<int:pk>/', ReportUpdateView.as_view(), name="update"),
    path('generate/', ReportGenerateView.generate_pdf, name="generate"),
], 'reports')

