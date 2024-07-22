from django.shortcuts import render , redirect
from django.http import HttpRequest
from .models import Plant
import os

# Create your views here.
def HomePage(request:HttpRequest):
    plant= Plant.objects.all()
    return render(request , 'Pages/Home.html' , {'plant':plant})

def DisplayAll(request:HttpRequest):
    plant= Plant.objects.all()
    return render(request , 'pages/All_Plants.html' , {"plant":plant})

def detail(request:HttpRequest , plant_id):
    plant=Plant.objects.get(pk=plant_id)
    
    return render(request , 'pages/detail.html', {'plant':plant})

def new(request:HttpRequest):
    if request.method == "POST":
        new_plants = Plant(name=request.POST['name'] , about=request.POST['about'] , used_for=request.POST['used_for'] , category=request.POST['category'] , is_edible=request.POST['is_edible'] , created_at = request.POST['created_at'] , image = request.FILES["image"])
        new_plants.save()
        return redirect("PagesPlanteer:HomePage")
    
    return render(request , 'pages/plants_new.html')

def update(request:HttpRequest , plants_id):
    plant=Plant.objects.get(pk=plants_id)
    if request.method == "POST":
        plant.name=request.POST['name']
        plant.about = request.POST['about']
        plant.used_for = request.POST['used_for']
        plant.category = request.POST['category']
        plant.is_edible = request.POST['is_edible']
        plant.created_at = request.POST['created_at']
        if "images" in request.FILES: plant.image=request.FILES['image']
        plant.save()
        return redirect("PagesPlanteer:HomePage")
    
    return render(request , 'pages/ubdate.html' , {'plant':plant})

def delete(request:HttpRequest , plants_id):
    plant=Plant.objects.get(pk=plants_id)
    if plant.image:
        if os.path.isfile(plant.image.path):
            os.remove(plant.image.path)
    plant.delete()
    return redirect('PagesPlanteer:HomePage')

def contact(request:HttpRequest):
    return render(request , 'DisplayAll.html')

def messages(request:HttpRequest):
    return render(request , 'DisplayAll.html')
