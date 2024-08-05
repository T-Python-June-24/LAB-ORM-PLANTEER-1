from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plant.models import Plants  #import plant class from another app to retrieving data form data base.
from main.models import Contact
def home_view(request: HttpRequest):
    plant = Plants.objects.all()[0:3]
    return render(request,"index.html", {"plants": plant} )

def allPlant_view(request: HttpRequest):
    plants = Plants.objects.all()
    # Filter by category
    category = request.GET.get('category')
    if category:
        plants = plants.filter(category=category)
    
    # Filter by edible status
    edible = request.GET.get('edible')
    if edible is not None:
        is_edible = edible.lower() == 'true'
        plants = plants.filter(is_edible=is_edible)
        
    return render(request,"allPlant.html", {"plants":plants} )

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

def search_view(request:HttpRequest):

    if "search" in request.GET:
        plant = Plants.objects.filter(name__contains= request.GET["search"])
    else:
        plant=[ ]

    
    return render(request, "searchPlant.html", {"plant":plant})