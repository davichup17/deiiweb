import django_tables2 as tables
from django_tables2_reports.tables import TableReport
from django.contrib.auth.models import User

class UsersTable(TableReport):
    class Meta:
        model = User
        exclude_from_report = ("username", "first_name", "last_name", "email")
