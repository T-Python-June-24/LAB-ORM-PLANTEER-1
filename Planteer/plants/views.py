from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Q
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


def all_plants_view(request: HttpRequest):
    category = request.GET.get("category")
    is_edible = request.GET.get("is_edible")

    plants = Plant.objects.all()

    if category:
        plants = plants.filter(category=category)
    if is_edible:
        plants = plants.filter(is_edible=True)

    return render(request, "plants/all_plants.html", {"plants": plants, "selected_category": category, "selected_is_edible": is_edible})



def plant_detail_view(request: HttpRequest, plant_id: int):
    plant = Plant.objects.get(pk=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(pk=plant_id)[:5] 
    return render(request, 'plants/plant_detail.html', {"plant": plant, "related_plants": related_plants})



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

def plant_search_view(request:HttpRequest):
    query = request.GET.get("q")
    if query:
        plants = Plant.objects.filter(Q(name__icontains=query))
        count = plants.count()
    else:
        plants = Plant.objects.none()
        count = 0

    return render(request, "plants/search.html", {"plants": plants, "count": count, "query": query})

