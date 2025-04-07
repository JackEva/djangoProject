from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import StudentForm,FacultyForm
from .models import Faculty
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password, check_password
import hashlib

def sha256_hash(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

@login_required(login_url='user_login')
def sample1(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
            return HttpResponse("Form submitted successfully")
    else:
        form = StudentForm()
    return render(request, "app/base.html", {"form": form})

@login_required(login_url='user_login')
def faculty(request):
    us = request.session.get('username')
    username = User.objects.get(username=us)
    res = Faculty.objects.filter(user=username)
    return render(request, 'app/faculty.html', context={'res': res, 'user':us})

@login_required(login_url='user_login')
def update_faculty(request, id):
    res = Faculty.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=res)
    if form.is_valid():
        form.save()
        return redirect('faculty')
    return render(request, 'app/faculty.html', context={'form': form})

@login_required(login_url='user_login')
def create_faculty(request):
    user = request.session.get('username')
    if request.method == "POST":
        fist_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email') 
        gender = request.POST.get('gender')
        username = User.objects.get(username=user)
        Faculty.objects.create(first_name=fist_name, last_name=last_name, age=age, email=email, gender=gender, user=username)
        return redirect('faculty')
    return render(request, 'app/faculty.html')

@login_required(login_url='user_login')
def delete_faculty(request, id):
    res = Faculty.objects.get(id=id)
    res.delete()
    return redirect('faculty')

def sample(request):
    return render(request, "app/sample.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            request.session['username']=username
            return redirect('faculty')  
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'app/loginPage.html')

@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return render(request, 'app/loginPage.html')


def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')

        if password == confirm_password:
            
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists")
            elif User.objects.filter(email=email).exists():
                return HttpResponse("Email already exists")
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('user_login')
        else:
           return HttpResponse("Passwords do not match ") 
        
    return render(request, 'app/register.html')