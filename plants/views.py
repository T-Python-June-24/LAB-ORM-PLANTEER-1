from django.shortcuts import render, redirect
from .models import Plant

def all_plants(request):
    plants = Plant.objects.all()
    return render(request, 'plants/all_plants.html', {'plants': plants})
    
def plant_details(request, id):
    plant = Plant.objects.get(id=id)
    
    # get 3 random plants as related plants, excluding the current plant
    related_plants = Plant.objects.exclude(id=id).order_by('?')[:3]
    
    return render(request, 'plants/plant_details.html', {'plant': plant, 'related_plants': related_plants})


def new_plant(request):
    
    if request.method == 'POST':
        new_plant = Plant()
        new_plant.name = request.POST['name']
        new_plant.about = request.POST['about']
        new_plant.used_for = request.POST['used_for']
        new_plant.image = request.FILES['image']
        new_plant.category = request.POST['category']
        new_plant.is_edible = request.POST.get('is_edible', False)
        
        new_plant.save()
        return redirect('plants:all_plants')
    else:
        return render(request, 'plants/new_plant.html')
    
def update_plant(request, id):
    plant = Plant.objects.get(id=id)
    if request.method == 'POST':
        plant.name = request.POST['name']
        plant.about = request.POST['about']
        plant.used_for = request.POST['used_for']
        plant.category = request.POST['category']
        plant.is_edible = request.POST.get('is_edible', False)
        
        if 'image' in request.FILES:
            plant.image = request.FILES['image']
        plant.save()
        return redirect('plants:plant_details', id=id)
    else:
        return render(request, 'plants/update_plant.html', {'plant': plant})
def delete_plant(request, id):
    plant = Plant.objects.get(id=id)
    plant.delete()
    return redirect('plants:all_plants')