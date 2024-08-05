from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from .models import Plants
from .forms import PlantForm
from django.urls import reverse, include


def createPlant_view(request:HttpRequest):
    plant = Plants.objects.all()
    if request.method == "POST":
        newPlant = Plants(name=request.POST['name'], about=request.POST['about'], used_for=request.POST['used_for'], image= request.FILES['image'], category=request.POST['category'], is_edible=request.POST['is_edible'] , created_at=request.POST['created_at'])
        newPlant.save()
        
    return render(request, "addPlant.html", {"plants":plant })


def deletePlant_view(request: HttpRequest, plant_id: int):
    plant = Plants.objects.get(id=plant_id)
    plant.delete()
    return redirect("plant:listAllPlant_view")


def listAllPlant_view(request:HttpRequest):
    plant = Plants.objects.all()
    return render(request, "listAllPlant.html" ,{"plants": plant})


def updatePlant_view(request:HttpRequest, plant_id: int):
    plant=Plants.objects.get(pk=plant_id)

    if request.method == "POST":
        plant.name = request.POST["name"]
        plant.about = request.POST["about"]
        plant.used_for = request.POST["used_for"]
        plant.category = request.POST["category"]
        plant.is_edible = request.POST["is_edible"]
        if "image" in request.FILES: plant.image = request.FILES["image"]
        plant.save()
        return redirect("main:plantDetail_view", plant_id=plant_id)
        
    return render(request,'updatePlant.html',{"plants": plant})


