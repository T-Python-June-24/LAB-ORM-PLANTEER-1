from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plant.models import Plants  #import plant class from another app to retrieving data form data base.

def home_view(request: HttpRequest):
    plant = Plants.objects.all()
    return render(request,"index.html", {"plants": plant} )

def allPlant_view(request: HttpRequest):
    return render(request,"allPlant.html" )

def plantDetail_view(request: HttpRequest):
    return render(request,"plantDetail.html" )

def contactUs_view(request: HttpRequest):
    return render(request,"contactUs.html" )

def contactUsMessages_view(request: HttpRequest):
    return render(request,"contactUsMessages.html" )
