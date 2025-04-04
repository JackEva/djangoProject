from django.urls import path, include
from . import views

urlpatterns = [
    path('sample',views.sample,name="jack"),
    path('faculty',views.faculty, name="faculty"),
    path('cfaculty',views.create_faculty, name="create_faculty")

]