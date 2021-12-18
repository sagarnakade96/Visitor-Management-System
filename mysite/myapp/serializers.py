from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Visitors,Employee

class VisitorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Visitors
        fields = ['fname','visiting_person','al_time','id','contact','in_office','location']


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['emp_id','fname','lname','deparment','location','contact_num']