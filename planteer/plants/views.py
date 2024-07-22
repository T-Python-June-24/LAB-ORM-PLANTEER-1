from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant, Contact
from .forms import PlantForm, ContactForm
# Create your views here.

def home(request):
    plants = Plant.objects.all()[:3]
    return render(request, 'plants/home.html')

def all_plants(request):
    plants = Plant.objects.all()
    return render(request, 'plants/all_plants.html', {'plants': plants})

def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    return render(request, 'plants/plant_detail.html', {'plant': plant})

def new_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_plants')
    else:
        form = PlantForm()
    return render(request, 'plants/new_plant.html', {'form': form})

def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plants/update_plant.html', {'form': form})

def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        plant.delete()
        return redirect('all_plants')
    return render(request, 'plants/delete_plant.html', {'plant': plant})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'plants/contact.html', {'form': form})

def contact_messages(request):
    messages = Contact.objects.all().order_by('-sent_at')
    return render(request, 'plants/contact_messages.html', {'messages': messages})
