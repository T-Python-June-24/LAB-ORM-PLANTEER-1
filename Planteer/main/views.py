from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plants.models import Plant





def home(request:HttpRequest):

    plants = Plant.objects.all()[:3]
    

    return render(request, 'main/home.html', {"plants" : plants} )




def contact(request:HttpRequest):

    return render(request, 'main/contact.html' )



# def messages(request:HttpRequest):
#     return render(request, 'main/messages.html')