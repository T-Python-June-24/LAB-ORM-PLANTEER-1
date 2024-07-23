from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Plant

# Create your views here.
def create_plant_view(request:HttpRequest):
    
  if request.method == "POST":
    is_edible = request.POST.get("is_edible") == 'on'
    new_plant = Plant(
      name=request.POST["name"], 
      about=request.POST["about"], 
      used_for=request.POST["used_for"], 
      image=request.FILES["image"], 
      category=request.POST["category"], 
      is_edible=is_edible)
    new_plant.save()

    return redirect('main:home_view')

  return render(request, "plants/create.html")


def all_plants_view(request:HttpRequest):
  plants = Plant.objects.all()
  return render(request, "plants/all_plants.html", {"plants": plants})


def plant_detail_view(request:HttpRequest, plant_id:int):

  plants = Plant.objects.get(pk=plant_id)
  return render(request, 'plants/plant_detail.html', {"plants" : plants})


def plant_delete_view(request:HttpRequest, plant_id:int):

    plant = Plant.objects.get(pk=plant_id)
    plant.delete()

    return redirect("main:home_view")

def plant_update_view(request: HttpRequest, plant_id: int):
    plant = Plant.objects.get(pk=plant_id)

    if request.method == "POST":
        plant.name = request.POST["name"]
        plant.about = request.POST["about"]
        plant.used_for = request.POST["used_for"]
        plant.category = request.POST["category"]
        plant.is_edible = 'is_edible' in request.POST

        if "image" in request.FILES:
            plant.image = request.FILES["image"]

        plant.save()
        return redirect("plants:plant_detail_view", plant_id=plant.id)

    return render(request, "plants/plant_update.html", {"plant": plant})
