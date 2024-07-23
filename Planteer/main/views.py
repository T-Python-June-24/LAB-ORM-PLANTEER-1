from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from plants.models import Plant

# Create your views here.
def home_view(request: HttpRequest):
  plants = Plant.objects.all()
  return render(request, "main/index.html", {"plants": plants})