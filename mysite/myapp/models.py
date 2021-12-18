from django.db import models

# Create your models here.
class Employee(models.Model):    
    emp_id = models.AutoField(primary_key=True, unique=True) 
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    deparment = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_num = models.IntegerField() 
    def __str__(self):
        return self.fname

class Visitors(models.Model):
    fname = models.CharField(max_length=100)
    contact = models.IntegerField(null=True,blank=True)
    visiting_person = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    al_time = models.TimeField()
    in_office =  models.BooleanField("Is in the Office", default=False)
   
    def __str__(self):
        return self.fname