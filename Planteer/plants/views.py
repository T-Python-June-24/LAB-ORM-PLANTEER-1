from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Plant
from datetime import datetime   

# Create your views here.

def add_plant_view(request:HttpRequest):
    if request.method == "POST":
        new_plant = Plant(name=request.POST["name"], about=request.POST["about"], used_for=request.POST["used_for"], category=request.POST["category"],is_edible=request.POST["is_edible"], created_at=datetime.now(), image=request.FILES['image'])
        new_plant.save()
        return redirect('main:home_view')
    return render(request, "plants/new.html")



def all_view(request: HttpRequest):
     #get all plants    
    plants = Plant.objects.all()
    return render(request, 'plants/all.html', {"plants" : plants})

    return render(request, 'main/index.html')


def detail_view(request: HttpRequest, plant_id:int):
    plant = Plant.objects.get(pk = plant_id)
    category = plant.category
    plantsByCat= Plant.objects.filter(category=category).exclude(pk = plant_id)

    return render(request, 'plants/detail.html', {'plant':plant, 'plantsByCat': plantsByCat})



def update_view(request:HttpRequest, plant_id:int):
    plant = Plant.objects.get(pk = plant_id)
    if request.method == 'POST':
        plant.name = request.POST['name']
        plant.about = request.POST['about']
        plant.created_at = datetime.now()
        plant.used_for = request.POST['used_for']
        plant.is_edible = request.POST['is_edible']
        plant.category = request.POST['category']
        if 'image' in request.FILES: plant.image = request.FILES['image']
        plant.save()
        return redirect('plants:detail_view', plant_id = plant.id)
    
    return render(request, 'plants/update.html', {'plant':plant})


def delete_view(request:HttpRequest, plant_id:int):
    plant = Plant.objects.get(pk = plant_id)
    plant.delete()

    return redirect('main:home_view')