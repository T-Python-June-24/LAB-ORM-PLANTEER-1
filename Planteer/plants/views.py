from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant

def add_plants(request:HttpRequest):

    if request.method == "POST":
        if request.POST.get('is_edible') == "on":
            is_edible= True
        else :
            is_edible = False
        new_plant = Plant(name=request.POST["name"], about=request.POST["about"], used_for=request.POST["used_for"], category=request.POST["category"], is_edible = is_edible, image=request.FILES["image"])
        new_plant.save()

    return render(request, 'plants/add_plants.html')

def all_view(request:HttpRequest):

    return render(request,"plants/all_plants.html")


def detail_view(request:HttpRequest,plant_id:int):

    plant = Plant.objects.get(pk=plant_id)

    return render(request,"plants/plant_detail.html",{"plant":plant})


def update_plant(request:HttpRequest,plant_id:int):

    plant = Plant.objects.get(pk=plant_id)
    print(request.POST.get('is_edible'))
    if request.POST.get('is_edible') == "on":
            is_edible= True
    else :
            is_edible = False
    if request.method == "POST":
        plant.name = request.POST["name"]
        plant.about = request.POST["about"]
        plant.used_for = request.POST["used_for"]
        plant.category = request.POST["category"]
        plant.is_edible = is_edible
        if "image" in request.FILES: plant.image = request.FILES["image"]

        plant.save()


        return redirect("plants:detail_view", plant_id=plant_id)

    return render(request,"plants/update_plant.html",{"plant":plant})

def delete_plant(request:HttpRequest,plant_id:int):

    plant = Plant.objects.get(pk=plant_id)

    plant.delete()


    return redirect("main:home_view")

    # return render(request,"plants/update_plant.html",{"plant":plant})