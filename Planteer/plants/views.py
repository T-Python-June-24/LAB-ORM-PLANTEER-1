from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plants.models import Plant

# Create your views here.

def all_plants(request:HttpRequest):

    Plants = Plant.objects.all()

    return render(request, 'plants/all_plants.html', {"Plants" : Plants} )


def add_plant(request: HttpRequest):
    if request.method == "POST":
        is_edible = request.POST.get('is_edible', 'off') == 'on'
        new_plant = Plant(
            name=request.POST.get("name"),
            about=request.POST.get("about"),
            used_for=request.POST.get("used_for"),
            is_edible=is_edible, 
            category=request.POST.get("category"),
            image=request.FILES.get("image") 
        )
        new_plant.save()
        return redirect('main:home_view')
    return render(request, "plants/add_plant.html")
def plant_detail(request:HttpRequest,plant_id:int):
    plant=Plant.objects.get(pk=plant_id)
    return render(request,"main/plant_detail.html",{"plant":plant})
# def update_plant
# def delete_plant  


