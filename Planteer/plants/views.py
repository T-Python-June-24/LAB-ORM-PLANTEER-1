from django.shortcuts import render, redirect
from .models import Plant, Category



def all_plants(request):

    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')

    plants = Plant.objects.all()
    if category:
        plants = plants.filter(category=category)
    if is_edible:
        plants = plants.filter(is_edible=(is_edible.lower() == 'true'))

    categories = Category.choices
    return render(request, 'plants/all_plants.html', {'plants': plants, 'categories': categories})



def create_plant(request):

    if request.method == "POST":
        new_plant = Plant(name = request.POST['name'],
            about = request.POST['about'],
            used_for = request.POST['used_for'],
            plant_image = request.FILES['plant_image'],
            category = request.POST['category'],
            is_edible = 'is_edible' in request.POST
        )
        
        new_plant.save()

        return redirect('main:home')
    return render(request, 'Plants/add_plant.html')




def plant_detail(request, plant_id):

    plant = Plant.objects.get(pk=plant_id)

    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:3]

    return render(request, 'Plants/plant_detail.html', {"plant" : plant, 'related_plants': related_plants})






def plant_update(request, plant_id):

    plant = Plant.objects.get(pk=plant_id)

    if request.method == 'POST':
        plant.name = request.POST['name']
        plant.about = request.POST['about']
        plant.used_for = request.POST['used_for']
        plant.category = request.POST['category']
        plant.is_edible = 'is_edible' in request.POST
        if 'plant_image' in request.FILES:
            plant.plant_image = request.FILES['plant_image']

        plant.save()

        return redirect('plants:plant_detail', plant_id=plant.id)
    categories = Category.choices
    return render(request, 'plants/update_plant.html', {'plant': plant, 'categories': categories})




def plant_delete(request, plant_id):

    plant = Plant.objects.get(pk=plant_id)

    if request.method == 'POST':
    
        plant.delete()

        return redirect('plants:all_plants')
    return render(request, 'plants/delete_plant.html', {'plant': plant})




def search(request):

    query = request.GET.get('q')

    if query:
        results = Plant.objects.filter(name__icontains=query)
        # results = Plant.objects.filter(name__icontains(query))
        count = results.count()
        
        return render(request, 'plants/search_results.html', {'results': results, 'count': count, 'query': query})
    return render(request, 'plants/search_results.html', {'results': None, 'query': query})
