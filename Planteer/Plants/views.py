from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Category, Plants
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError



def plants(request: HttpResponse):
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')
    plants = Plants.objects.all()

    if category:
        plants = plants.filter(category=category)
    if is_edible:
        plants = plants.filter(is_edible=(is_edible.lower() == 'true'))

    return render(request, 'Plants/all_plants.html', {'plants': plants , 'categories': Category.choices})


def search_plant(request: HttpResponse):
    query = request.GET.get('query')
    if query:
        plants = Plants.objects.filter(name__icontains=query)
        count = plants.count()
    else:
        plants = Plants.objects.all()[:3]
        count = None

    return render(request, 'Plants/search_plants.html', {'plants': plants, 'count': count, 'query': query})

def add_plant(request:HttpResponse):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            about = request.POST['about']
            used_for = request.POST['used_for']
            plant_image = request.FILES['plant_image']
            category = request.POST['category']
            is_edible = 'is_edible' in request.POST

            plant = Plants(
                name=name,
                about=about,
                used_for=used_for,
                plant_image=plant_image,
                category=category,
                is_edible=is_edible
            )
            plant.save()
            messages.success(request, 'Plant added successfully!')
        except MultiValueDictKeyError as e:
            messages.error(request, f'Missing field: {str(e)}')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
        return redirect('Contact:thanks_add_plant')
    return render(request, 'Plants/add_plant.html')





def plant_detail(request: HttpResponse, plant_id: int):
    plant = get_object_or_404(Plants, pk=plant_id)
    selected_plant = Plants.objects.filter(is_edible=plant.is_edible)[:3]
    return render(request, 'Plants/plant_detail.html', {'plant': plant , 'selected_plant': selected_plant})


def update_plant(request: HttpResponse, plant_id: int):
    plant = get_object_or_404(Plants, pk=plant_id)

    if request.method == 'POST':
        try:
            plant.name = request.POST.get('name', plant.name)
            plant.about = request.POST.get('about', plant.about)
            plant.used_for = request.POST.get('used_for', plant.used_for)
            if 'plant_image' in request.FILES:
                plant.plant_image = request.FILES['plant_image']
            plant.category = request.POST.get('category', plant.category)
            plant.is_edible = 'is_edible' in request.POST

            plant.save()
            messages.success(request, 'Plant updated successfully!')
            return redirect('Plants:plant_detail', plant_id=plant.id)
        except MultiValueDictKeyError as e:
            messages.error(request, f'Missing field: {str(e)}')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')

    return render(request, 'Plants/update_plant.html', {'plant': plant})



def delete_plant(request: HttpResponse, plant_id: int):
    plant = get_object_or_404(Plants, pk=plant_id)

    if request.method == 'POST':
        plant.delete()
        messages.success(request, 'Plant deleted successfully!')
        return redirect('Plants:plants')

    return render(request, 'Plants/delete_plant.html', {'plant': plant})