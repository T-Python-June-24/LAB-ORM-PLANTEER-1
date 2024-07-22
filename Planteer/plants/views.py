from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from plants.models import Plant

# Create your views here.
def all_plants(request):
    Plants = Plant.objects.all()

    category = request.GET.get('category')
    if category:
        Plants = Plants.filter(category=category)

    is_edible = request.GET.get('is_edible')
    if is_edible:
        Plants = Plants.filter(is_edible=(is_edible == 'True'))

    return render(request, 'plants/all_plants.html', {'Plants': Plants})


def add_plant(request: HttpRequest):
    if request.method == "POST":
        is_edible = request.POST.get('is_edible', 'off') == 'on'
        new_plant = Plant(
            name=request.POST["name"],
            about=request.POST["about"],
            used_for=request.POST["used_for"],
            is_edible=is_edible, 
            category=request.POST["category"],
            image=request.FILES["image"] 
        )
        new_plant.save()
        return redirect('main:home_view')
    return render(request, "plants/add_plant.html")
def plant_detail(request:HttpRequest,plant_id:int):

    plant=Plant.objects.get(pk=plant_id)
    plant_category=plant.category

    Plants = Plant.objects.all()
    filterPlants = Plants.filter(category=plant_category)
    return render(request,"plants/plant_detail.html",{"plant":plant,"filterPlants":filterPlants})

def delete_plant(request:HttpRequest,plant_id:int):
    plant=Plant.objects.get(pk=plant_id)
    plant.delete()
    return redirect('main:home_view')
def update_plant (request:HttpRequest,plant_id:int):
        plant=Plant.objects.get(pk=plant_id)
        if request.method=="POST":
            plant.name=request.POST["name"]
            plant.about=request.POST["about"]
            plant.used_for=request.POST["used_for"]
            plant.is_edible= request.POST.get('is_edible', 'off') == 'on'
            plant.category=request.POST["category"]
            if "image" in request.FILES :
                plant.image=request.FILES["image"] 
            plant.save()
            return redirect('plants:plant_detail',plant_id=plant.id)

        return render(request,"plants/update_plant.html",{"plant":plant})  
def plants_search(request:HttpRequest):
     if request.method=="POST":
          searched=request.POST['searched']
          plant = Plant.objects.filter(name__contains=searched)
          count=len(plant)
          return render(request, 'plants/plants_search.html',{'searched':searched, 'plant':plant , 'count':count})
     else:
          return render(request, 'plants/plants_search.html')
