from django.contrib import admin
from .models import Employee,Visitors

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','emp_id','deparment','location']

class VisitorsAdmin(admin.ModelAdmin):
    list_display=['fname','visiting_person','al_time','in_office',]



admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Visitors,VisitorsAdmin)