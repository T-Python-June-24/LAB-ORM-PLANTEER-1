from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def HomePage(request:HttpRequest):
    return render(request , 'index.html')

def DisplayAll(request:HttpRequest):
    return render(request , 'DisplayAll.html')

def detail(request:HttpRequest):
    return render(request , 'DisplayAll.html')

def new(request:HttpRequest):
    return render(request , 'DisplayAll.html')

def update(request:HttpRequest):
    return render(request , 'DisplayAll.html')

def delete(request:HttpRequest):
    return render(request , 'DisplayAll.html')

def contact(request:HttpRequest):
    return render(request , 'DisplayAll.html')

def messages(request:HttpRequest):
    return render(request , 'DisplayAll.html')
