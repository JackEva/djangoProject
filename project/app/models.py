from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    # gender = models.CharField(max_length=100)
    attendance = models.CharField(max_length=100,null=True)

class Faculty(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)   
    class Meta: 
        db_table = 'faculty_table'


class employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_designation = models.CharField(max_length=100)
    emp_department = models.CharField(max_length=100)
    emp_salary = models.IntegerField()
    emp_age = models.IntegerField()
    emp_email = models.EmailField()

    class Meta:
        db_table = 'employee_table'
  
class user(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = 'user_table'