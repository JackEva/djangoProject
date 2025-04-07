from django.forms import ModelForm
from .models import Student,Faculty
from django.contrib.auth.models import User

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'attendance']
    
class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = ['first_name','last_name','age','email']

class userLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']