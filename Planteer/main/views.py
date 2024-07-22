from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plants.models import Plant

def home_view(request:HttpRequest):

    plants = Plant.objects.all()

    return render(request, 'main/home.html',{"plants":plants})




