from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from string import Template
# Create your views here.


class ReportListView(ListView):
    model = Report
    template = 'report/report_list.html'


class ReportCreateView(CreateView):
    model = Report
    fields = ('name', 'description', 'template')
    success_url = reverse_lazy('reports:reports')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ReportUpdateView(UpdateView):
    model = Report
    fields = ('name', 'description', 'template')
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('reports:update', args=[self.object.id])
        
class ReportGenerateView(DetailView):

    def get(self, request, *args, **kwargs):
        print(request)

    def generate_pdf(self):
        print("eheheheh\n")
        print(self.request)

    def replace_variables(text, variables):
        if not text:
            return ''
        tpl = Template(text)
        result = tpl.safe_substitute(variables)
        return result