from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from plants import Plant



# Create your views here.
def index(request):
    plants = Plant.objects.all()
    return render(request, 'main/index.html', {'plants': plants})
    # return render(request, 'main/index.html')
