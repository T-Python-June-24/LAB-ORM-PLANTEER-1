from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant, Contact
from .forms import PlantForm, ContactForm

def home(request):
    plants = Plant.objects.all()[1:4] 
    return render(request, 'home.html', {'plants': plants})

def all_plants(request):
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')
    plants = Plant.objects.all()
    
    if category:
        plants = plants.filter(category=category)
    if is_edible:
        plants = plants.filter(is_edible=is_edible)
    
    return render(request, 'all_plants.html', {'plants': plants})

def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(pk=plant_id)[:5]
    return render(request, 'plant_detail.html', {'plant': plant, 'related_plants': related_plants})

def add_plant(request):
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_plants')
    else:
        form = PlantForm()
    return render(request, 'plant_form.html', {'form': form})

def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == "POST":
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plant_form.html', {'form': form})

def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == "POST":
        plant.delete()
        return redirect('all_plants')
    return render(request, 'plant_confirm_delete.html', {'plant': plant})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_messages(request):
    messages = None
    error = None
    
    if request.method == "POST":
        password = request.POST.get('password')
        if password == 'admin':
            messages = Contact.objects.all()
        else:
            error = 'Invalid password'
    return render(request, 'contact_messages.html', {'messages': messages, 'error': error})

def search_plants(request):
    query = request.GET.get('q')
    results= Plant.objects.filter(name__icontains=query) if query else None
    return render(request, 'search_results.html', {'results':results, 'query':query})
