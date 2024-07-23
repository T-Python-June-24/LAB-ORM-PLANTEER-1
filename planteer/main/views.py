from django.shortcuts import render,redirect
from django.http import HttpRequest
from . import models 
# from models import Plant , Contact , PlantChoices
# Create your views here.
def home_view(request:HttpRequest):
    plants=models.Plant.objects.all()[0:3]
    return render(request,"main/index.html",{"plants":plants})

def add_plant_view(request:HttpRequest)->render:
    if request.method=='POST':
        name=request.POST["name"]
        about=request.POST["about"]
        used_for=request.POST["used_for"]
        image=request.FILES["image"]
        category=request.POST["category"]
        is_edible= True if request.POST["is_edible"] =="True"  else False
        plane=models.Plant(name=name,about=about,used_for=used_for,category=category,is_edible=is_edible, image=image)
        plane.save()
        return  redirect("main:home_view")
    
    choices = models.Plant.PlantChoices.choices
    return render(request,'main/add_plant.html',{"choices":choices})




def all_plant_view(request: HttpRequest):
    ediblity = request.GET.get("edible", "all")  # Get 'edible' from query string
    if ediblity == "all":
        plants = models.Plant.objects.all()
    elif ediblity == "true":
        plants = models.Plant.objects.filter(is_edible=True)
    elif ediblity == "false":
        plants = models.Plant.objects.filter(is_edible=False)
    return render(request, "main/all_plant.html", {"plants": plants})



def plant_detail_view(request,plant_id):
    selected_plant=models.Plant.objects.get(pk=plant_id)
    category=selected_plant.category
    suggestion=models.Plant.objects.filter(category=category)
    return render(request,"main/plant_detail.html",{"plant":selected_plant,"sug":suggestion})

def update_plant_view(request: HttpRequest, plant_id):
    plant = models.Plant.objects.get(pk=plant_id)
    existing_image_url = plant.image.url if plant.image else None  # Get existing image URL

    if request.method == 'POST':
        name = request.POST["name"]
        about = request.POST["about"]
        used_for = request.POST["used_for"]
        image = request.FILES.get("image")  # Use get() to handle potentially missing image
        category = request.POST["category"]
        is_edible = True if request.POST["is_edible"] == "true" else False

        plant.name = name
        plant.about = about
        plant.used_for = used_for
        plant.category = category
        plant.is_edible = is_edible

        if image:  # Update image only if a new one is uploaded
            plant.image = image
        else:
            # User didn't upload a new image, keep the existing one
            pass  

        plant.save()
        return redirect("main:home_view")

    choices = models.Plant.PlantChoices.choices  # Get choices outside the POST block
    return render(request, "main/update_plant.html", {"plant": plant, "choices": choices})

def delete_plant_view(request:HttpRequest,plant_id:int):
    plant=models.Plant.objects.get(pk=plant_id)
    plant.delete()
    return redirect("main:home_view")

def contact_view(request:HttpRequest):
    if request.method=="POST":
       contact=models.Contact(
                            first_name=request.POST["first_name"],
                            last_name=request.POST["last_name"],
                            email=request.POST["email"],
                            message=request.POST["message"]
                              )
       contact.save()
    return render(request,"main/contact.html")

def contact_messages_view(reuqest:HttpRequest):
    message=models.Contact.objects.all()
    return render(reuqest,"main/contact_message.html",{"message":message})

def plant_search_view(request:HttpRequest):
    plants = None
    count = 0  
    if request.method == "POST":
        searched = request.POST["search"]
        plants = models.Plant.objects.filter(name__contains=searched)
        count = plants.count()  # Count plants after filtering

    return render(request, "main/plant_search.html", {"plants": plants, "count": count})