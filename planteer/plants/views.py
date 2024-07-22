from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Plants,contact



def plant_list_view(request:HttpRequest):
        
    if request.method == "POST":
        new_plant = Plants(name=request.POST["name"], about=request.POST["about"], used_for=request.POST["used_for"], images=request.FILES["images"], category=request.POST["category"], is_edible=request.POST["is_edible"],created_at=request.POST["created_at"])
        new_plant.save()
        return redirect('main:home_view')
    return render(request , "plants/plant.html")
    


def contact_list_view(request:HttpRequest):
        
    if request.method == "POST":
        new_contact =contact(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"],message=request.POST["message"])
        new_contact.save()
        return redirect('main:home_view')
    return render(request , "plants/contact.html")


def all_plant_view(request:HttpRequest):
    plant=Plants.objects.order_by("-created_at")
    print(Plants.objects.count())
    return render (request , "plants/all_plant.html", {"plant" : plant})



def plant_detail_view(request:HttpRequest , plant_id:int):

    plant=Plants.objects.get(pk=plant_id)

    return render(request , "plants/plant_detail.html" , {"plant" : plant})


def plant_update_view(request:HttpRequest , plant_id:int):
    plant=Plants.objects.get(pk=plant_id)

    if request.method=="POST":
        plant.name=request.POST["name"]
        plant.about=request.POST["about"]
        plant.used_for=request.POST["used_for"]
        plant.category=request.POST["category"]
        plant.is_edible=request.POST["is_edible"]
        plant.created_at=request.POST["created_at"]

        if "images" in request.FILES: plant.images = request.FILES["images"]

        plant.save()



        return redirect("plants:plant_detail_view", plant_id=plant.id)

    return render(request , "plants/plant_update.html" , {"plant" : plant})

def plant_delete_view(request:HttpRequest , plant_id:int):
    plant=Plants.objects.get(pk=plant_id)
    plant.delete()
    return redirect("main:home_view")
