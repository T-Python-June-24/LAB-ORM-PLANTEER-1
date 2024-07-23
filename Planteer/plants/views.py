from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant


# Create your views here.
def all(request: HttpRequest) -> HttpResponse:
    return render(request, 'plants/all.html')


def details(request: HttpRequest) -> HttpResponse:
    return render(request, 'plants/details.html')


def add(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        new_plant = Plant(name=request.POST['name'], about=request.POST['about'], used_for=request.POST['used_for'],
                          image=request.FILES['image'], category=request.POST['category'],
                          is_edible=request.POST.get('is_edible') == 'on')
        new_plant.save()
        return redirect('main:index')
    return render(request, 'plants/add.html')


def update(request: HttpRequest) -> HttpResponse:
    return render(request, 'plants/update.html')
