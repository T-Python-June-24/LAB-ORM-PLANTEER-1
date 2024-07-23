from django.shortcuts import render , redirect
from django.http import HttpRequest
from .models import Plant
from django.db.models import Q
import os

# Create your views here.
def HomePage(request:HttpRequest):
    plant= Plant.objects.all()[0:3]
    return render(request , 'Pages/Home.html' , {'plant':plant})

def DisplayAll(request:HttpRequest):
    plant= Plant.objects.all()
    return render(request , 'pages/All_Plants.html' , {"plant":plant})

def detail(request:HttpRequest , plant_id):
    plant=Plant.objects.get(pk=plant_id)
    plants = Plant.objects.filter(category=plant.category).exclude(pk=plant_id)
    return render(request , 'pages/detail.html', {'plant':plant , 'plants':plants})

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
        if "image" in request.FILES: plant.image=request.FILES['image']
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

def search(request:HttpRequest):
    if request.method == 'GET':
        word_search=request.GET['search']
        plants=Plant.objects.filter(name__contains = request.GET['search'])
        count_plants=plants.count()
        return render(request , 'pages/search.html', {'plant':plants , "count_plants":count_plants , "word_search":word_search})
    return render(request , 'pages/search.html')
def filtering(request:HttpRequest):
    if request.method == 'POST':
        category_get=request.POST['category']
        is_edible_get=request.POST['is_edible']
        filtered=Q()
        if category_get:
            filtered &= Q(category = request.POST['category'])
        if is_edible_get in ['True', 'False']:
            filtered &= Q(is_edible = request.POST['is_edible'])
        plants=Plant.objects.filter(filtered)
        count_plants=plants.count()
        return render(request , 'pages/All_Plants.html', {'plant':plants , "count_plants":count_plants})