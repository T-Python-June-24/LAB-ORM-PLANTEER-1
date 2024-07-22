from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import plant

def add_plants(request:HttpRequest):

    if request.method == "POST":
        if request.POST.get('is_edible') == "on":
            is_edible= True
        else :
            is_edible = False
        new_plant = plant(name=request.POST["name"], about=request.POST["about"], used_for=request.POST["used_for"], category=request.POST["category"], is_edible = is_edible, image=request.FILES["image"])
        new_plant.save()

    return render(request, 'plants/add_plants.html')




