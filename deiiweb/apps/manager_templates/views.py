from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import TemplateForm
from django.core.files.storage import FileSystemStorage
from .models import Template
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

'''def upload_file(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'manager_templates/upload.html', context)

def template_list(request):
    templates = Template.objects.all()

    return render(request, 'manager_templates/template_list.html', {
        'templates': templates
    })

def upload_template(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('template_list')
    else:
        form = TemplateForm()
    return render(request, 'manager_templates/upload_template.html', {
        'form' : form
    })'''

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class TemplateListView(ListView):
    model = Template
    template = 'manager_templates/template_list.html'

@method_decorator(staff_member_required, name='dispatch')
class TemplateCreateView(CreateView):
    model = Template
    fields = '__all__'
    form = TemplateForm
    success_url = reverse_lazy('templates:templates')

@method_decorator(staff_member_required, name='dispatch')
class TemplateUpdateView(UpdateView):
    model = Template
    fields = ['name', 'content']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('templates:update', args=[self.object.id, self.object.name]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')       
class TemplateDeleteView(DeleteView):
    model = Template
    template = 'manager_templates/template_confirm_delete.html'
    success_url = reverse_lazy('templates:templates')

'''class FileFieldView(FormView):
    form_class = UploadFileForm
    template_name = 'manager_templates/upload.html' 
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})'''