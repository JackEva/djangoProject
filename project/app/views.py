from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import StudentForm,FacultyForm
from .models import Faculty


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

def faculty(request):
    res = Faculty.objects.all()
    Faculty.objects.filter()
    


    
    return render(request, 'app/faculty.html', context={'res': res})


def update_faculty(request, id):
    res = Faculty.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=res)
    if form.is_valid():
        form.save()
        return redirect('faculty')
    return render(request, 'app/faculty.html', context={'form': form})

def create_faculty(request):
    if request.method == "POST":
        fist_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email') 
        gender = request.POST.get('gender')
        Faculty.objects.create(first_name=fist_name, last_name=last_name, age=age, email=email, gender=gender)
        return redirect('faculty')
    return render(request, 'app/faculty.html')


def delete_faculty(request, id):
    res = Faculty.objects.get(id=id)
    res.delete()
    return redirect('faculty')

def sample(request):
    return render(request, "app/sample.html")