from django.db import models
from django.contrib import admin
class Student(models.Model):
    student_name = models.CharField(max_length=250, help_text="Enter the student name")
    age= models.IntegerField(help_text="Enter age between 18 to 22")
    dob = models.DateField(help_text="Enter the dob")
    genre = models.CharField(max_length=50, help_text="Genre")
    reg_num=models.IntegerField(help_text="Enter the register.no")

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name','age','dob','genre','reg_num')
# Create your models here.
