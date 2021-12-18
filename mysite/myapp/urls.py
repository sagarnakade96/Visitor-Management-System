"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('emp_details',views.emp_details,name="emp_details"),
    path('add_details',views.add_details,name="add_details"),
    path('visitors',views.visitors,name="visitors"),
    path('vis_prof',views.vis_prof,name="vis_prof"),
    path('update_emp/<emp_id>',views.update_emp,name="update_emp"),
    path('delete_emp/<emp_id>',views.delete_emp,name="delete_emp"),
    path('update_vis/<vis_id>',views.update_vis,name="update_vis"),
    path('delete_vis/<vis_name>',views.delete_vis,name="delete_vis"),
    
]
