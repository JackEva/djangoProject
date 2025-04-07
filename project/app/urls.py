from django.urls import path, include
from . import views

urlpatterns = [
    path('sample/',views.sample,name="jack"),
    path('faculty/',views.faculty, name="faculty"),
    path('cfaculty/',views.create_faculty, name="create_faculty"),
    path('delete/<int:id>',views.delete_faculty, name="delete_faculty"),
    path('login/',views.user_login, name="user_login"),
    path('logout/',views.user_logout, name="user_logout"),
    path('register/',views.user_register, name="user_register"),

    # path('update/<int:id>',views.update_faculty, name="update_faculty"),


]    