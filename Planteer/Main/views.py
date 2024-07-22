from django.shortcuts import render,redirect
from django.http import HttpResponse

from Plants.models import Plants
# Create your views here.

def home(request:HttpResponse):
    plants_list = Plants.objects.all()[:3]
    return render(request, 'Main/Main.html',{'plants':plants_list})
