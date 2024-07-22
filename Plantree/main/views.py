from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest):
    return render(request,"home.html" )

def allPlant_view(request: HttpRequest):
    return render(request,"allPlant.html" )

def plantDetail_view(request: HttpRequest):
    return render(request,"plantDetail.html" )

def contactUs_view(request: HttpRequest):
    return render(request,"contactUs.html" )

def contactUsMessages_view(request: HttpRequest):
    return render(request,"contactUsMessages.html" )
