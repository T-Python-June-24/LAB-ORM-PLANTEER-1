from django.shortcuts import render, redirect
from .models import Plant

def all_plants(request):
    category = request.GET.get('category', 'all')
    edible = request.GET.get('edible', 'all')
    plants = Plant.objects.all()
    
    if category != 'all':
        plants = plants.filter(category=category)
    if edible != 'all':
        plants = plants.filter(is_edible=edible)
    
    categories = Plant.objects.values_list('category', flat=True).distinct()
    return render(request, 'plants/all_plants.html', {'plants': plants, 'categories': categories, 'selected_category': category, 'selected_edible': edible})
    
def plant_details(request, id):
    plant = Plant.objects.get(id=id)
    
    
    related_plants = Plant.objects.filter(category=plant.category, is_edible=plant.is_edible).exclude(id=id).order_by('?')[:3]
    
    return render(request, 'plants/plant_details.html', {'plant': plant, 'related_plants': related_plants,})


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


def search_plants(request):
    query = request.GET.get('query')
    plants = Plant.objects.filter(name__icontains=query)
    num_results = plants.count()
    return render(request, 'plants/search_results.html', {'plants': plants, 'num_results': num_results})