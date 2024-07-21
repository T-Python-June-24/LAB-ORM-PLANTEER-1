from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.



def home(request:HttpResponse):
    return render(request, 'Main/Main.html')
