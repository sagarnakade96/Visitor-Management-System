from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Employee,Visitors

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields='__all__'

class VisitorsForm(ModelForm):
    class Meta:
        model = Visitors
        fields='__all__'