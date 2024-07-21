from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Plants
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def plants(request:HttpResponse):
    plants = Plants.objects.all()
    return render(request, 'Plants/all_plants.html',{'plants':plants})


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


