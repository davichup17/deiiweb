from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django import views
from django_tables2 import SingleTableView
#class based view import for list User
from django.views.generic.list import ListView
#class based view import for displaying User
from django.views.generic.detail import DetailView
#class based view import for editing User
from django.views.generic.edit import UpdateView

from .tables import UsersTable

class HomePageView(TemplateView):
    template_name = "core/index.html"

#List Views
class UserListView(SingleTableView):
    """
    Class to list all the user
    """
    model = User
    table_clas = UsersTable
    template_name = "core/user_list.html"

'''# Detail Views
class UserDetailView(DetailView):
    """
    Class to display user profile in detail
    """
    model = User
    template_name = "profiles/user_detail.html"
    #use username instead of pk
    slug_field = "username"
    #override the context user object from user to user_profile, use {{ user_profile }} instead of {{ user }} in template
    context_object_name = "user_profile"

#From Views
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    """
    Class that only allows authentic user to update their account
    username, email
    """
    model = User
    form_class = AccountForm
    template_name = "profiles/user_account_edit.html"
    success_url = "."
    slug_field = "username"
    def get_queryset(self):
        base_qs = super(ProfileUpdateView, self).get_queryset()
        return base_qs.filter(username=self.request.user.username)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Class that only allows authentic user to update their profile
    Composed of first_name,last_name,date_of_birth,gender,
    """
    model = User
    form_class = ProfileForm
    template_name = "profiles/user_profile_edit.html"
    success_url = "."
    slug_field = "username"
    def get_queryset(self):
        base_qs = super(ProfileUpdateView, self).get_queryset()
        return base_qs.filter(username=self.request.user.username)'''