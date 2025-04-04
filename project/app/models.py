from django.db import models

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
  