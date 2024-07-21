from django.shortcuts import render
from plants.models import Plant

# Create your views here.

def home_view(request):
    plants = Plant.objects.all()
    return render(request, 'main/home.html', {'plants': plants})