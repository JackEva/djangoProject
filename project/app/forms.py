from django.forms import ModelForm
from .models import Student,Faculty

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'attendance']
    
class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = ['first_name','last_name','age','email']