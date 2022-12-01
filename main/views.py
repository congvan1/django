from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Teacher, Class
# Create your views here.
def index(response):
    #person = Student.objects.get(id=id)
    
    return render(response, 'main/home.html', {})

def home(response):
    return render(response, 'main/home.html', {})

def profile(response):
    #u = user.student.all()
    return render(response, 'main/profile.html', {})