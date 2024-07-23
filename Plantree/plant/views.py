from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Plants
from .forms import PlantForm

def createPlant_view(request:HttpRequest):
    plant = Plants.objects.all()
    if request.method == "POST":
        newPlant = Plants(name=request.POST['name'], about=request.POST['about'], used_for=request.POST['used_for'], image= request.FILES['image'], category=request.POST['category'], is_edible=request.POST['is_edible'] == False, created_at=request.POST['created_at'])
        newPlant.save()
        
    return render(request, "addPlant.html", {"plants":plant })


def deletePlant_view(request: HttpRequest, plant_id: int):
    plant = Plants.objects.get(id=plant_id)
    if request.method == "POST":
        plant.delete()
        return redirect('/plant/listAll/plant')
    return render(request, "deletePlant.html", {"plants": plant})


def listAllPlant_view(request:HttpRequest):
    plant = Plants.objects.all()
    return render(request, "listAllPlant.html" ,{"plants": plant})


def updatePlant_view(request:HttpRequest , plant_id: int):
    plant=Plants.objects.get(id=plant_id)
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
    mydict= {'form':form}
    return render(request,'updatePlant.html',context=mydict)


