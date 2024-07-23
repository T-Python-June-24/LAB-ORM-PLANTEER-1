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

    plants = Plant.objects.all()

    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')

    if category:
        plants = plants.filter(category=category)
    if is_edible:
        plants = plants.filter(is_edible=is_edible == 'True')

    categories = Plant.objects.values_list('category', flat=True).distinct()

    return render(request, "plants/all_plants.html", {
        "plants": plants,
        "categories": categories,
        "selected_category": category,
        "selected_is_edible": is_edible
    })

    # return render(request,"plants/all_plants.html",{"plants":plant})


def detail_view(request:HttpRequest,plant_id:int):

    plant = Plant.objects.get(pk=plant_id)
    category_plants = plant.category 

    plants = Plant.objects.all()
    
    related_plants = plants.filter(category=category_plants).exclude(pk=plant_id)

    return render(request,"plants/plant_detail.html",{"plant":plant,"related_plants":related_plants})


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


def search_plants(request:HttpRequest):

    if request.method == "POST":

        search = request.POST["search"]

        plants = Plant.objects.filter(name__contains=search)

        count = plants.count()

        return render(request,"plants/search.html",{"search":search,"plants":plants,"count":count})