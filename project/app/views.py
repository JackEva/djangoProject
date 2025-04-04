from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Faculty


def sample(request):
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
    Faculty.objects.create(
        first_name = 'John1',
        last_name = 'Doe',
        age = 30,
        email = 'venkatra0@gmail.com', 
        gender = 'male',
    )
    return redirect('faculty')


def delete_faculty(request, id):
    res = Faculty.objects.get(id=id)
    res.delete()
    return redirect('faculty')