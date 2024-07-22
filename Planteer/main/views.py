from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# from plants.models import plant

def home_view(request:HttpRequest):


    return render(request, 'main/home.html')


def contact_view(request:HttpRequest):

    return render(request, 'main/contact.html' )


def message_view(request:HttpRequest):

    return render(request, 'main/message.html' )


