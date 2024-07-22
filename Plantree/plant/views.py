from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Plants

def createPlant_view(request:HttpRequest):
    return render(request, "addPlant.html")

def deletePlant_view(request:HttpRequest):
    return render(request, "deletePlant.html")

def updatePlant_view(request:HttpRequest):
    return render(request, "updatePlant.html")

