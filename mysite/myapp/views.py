from django.shortcuts import redirect, render
from .models import Employee,Visitors
from .forms import EmployeeForm,VisitorsForm
from rest_framework.response import Response
from django.http import JsonResponse, response
from .serializers import EmployeeSerializers, VisitorsSerializers
from rest_framework.decorators import api_view
# Create your views here.
def home(request):
    return render(request,'index.html')

@api_view(['GET'])
def emp_details(request):
    empData = Employee.objects.all()
    data = EmployeeSerializers(empData,many=True).data
    context = {
        'data':data
    }
    return render(request,'./emp/emp.html',context)

def update_emp(request,emp_id):
    empData = Employee.objects.get(pk=emp_id)
    empForm = EmployeeForm(request.POST or None,instance=empData)
    if empForm.is_valid():
        empForm.save()
        return redirect('emp_details')
    context = {
        'empData':empData,
        'empForm' : empForm
    }

    return render(request, './emp/update_emp.html',context)


def update_vis(request,vis_id):
    visData = Visitors.objects.get(pk=vis_id)
    visForm = VisitorsForm(request.POST or None,instance=visData)
    if visForm.is_valid():
        visForm.save()
        return redirect('visitors')
    context = {
        'visData':visData,
        'visForm' : visForm
    }

    return render(request, './vis/update_vis.html',context)

def delete_emp(request,emp_id):
    empData = Employee.objects.get(pk=emp_id)
    empData.delete()
    return redirect('emp_details')

def delete_vis(request,vis_name):
    visData = Visitors.objects.filter(fname=vis_name)
    visData.delete()
    return redirect('visitors')


def add_details(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        deparment = request.POST['deparment']
        location = request.POST['location']
        contact_num = request.POST['contact_num']
        #creating user
        data_auth= Employee(fname=fname,
        lname=lname,
        deparment=deparment,
        location=location,
        contact_num=contact_num)        
        data_auth.save()
        return redirect('emp_details')
    return render(request,'./emp/prof.html')

@api_view(['GET'])
def visitors(request):
    vis_data = Visitors.objects.all()
    data = VisitorsSerializers(vis_data,many=True).data
    context = {
        'data':data
    }
    return render(request,'./vis/vis.html',context)

def vis_prof(request):
    if request.method == 'POST':
            fname = request.POST['fname']
            visiting_person = request.POST['visiting_person']
            
            location = request.POST['location']
            al_time = request.POST['al_time']  
            contact = request.POST['contact']           
            flexRadioDefault = request.POST['flexRadioDefault']
            if flexRadioDefault == 'a':
                in_office=True
            elif flexRadioDefault=='na':
                in_office = False
            #creating user
            data= Visitors(fname=fname,
            visiting_person=visiting_person,
            location=location,
            
            al_time=al_time,
            in_office=in_office,
            contact=contact)        
            data.save()
            return redirect('visitors')
    return render(request,'./vis/vis_prof.html')

