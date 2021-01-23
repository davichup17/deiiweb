from django.urls import path
from .views import *

templates_patterns = ([
    path('', TemplateListView.as_view(), name="templates"),
    path('create/', TemplateCreateView.as_view(), name="create"),
    path('update/<int:pk>/<slug:slug>/', TemplateUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', TemplateDeleteView.as_view(), name="delete"),
], 'templates')

'''path('templates/', template_list, name="template_list")'''