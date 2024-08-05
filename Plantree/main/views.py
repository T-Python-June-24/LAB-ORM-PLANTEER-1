from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plant.models import Plants  #import plant class from another app to retrieving data form data base.
from main.models import Contact
def home_view(request: HttpRequest):
    plant = Plants.objects.all()[0:3]
    return render(request,"index.html", {"plants": plant} )

def allPlant_view(request: HttpRequest):
    plant = Plants.objects.all()
    return render(request,"allPlant.html", {"plants":plant} )

def plantDetail_view(request: HttpRequest, plant_id: int):
    plant = Plants.objects.get(id=plant_id)
    plant2 = Plants.objects.filter(category=plant.category)
    print(F"The Category is {plant2}")
    return render(request,"plantDetail.html", {"plants": plant, "plants2": plant2})

def contactUs_view(request: HttpRequest):
    message = Contact.objects.all()
    if request.method == "POST":
        newMessage = Contact(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], message= request.POST['message'])
        newMessage.save()
    return render(request,"contactUs.html" , {"messages":message })

def contactUsMessages_view(request: HttpRequest):
    message = Contact.objects.all()
    return render(request,"contactUsMessages.html", {"messages":message } )
