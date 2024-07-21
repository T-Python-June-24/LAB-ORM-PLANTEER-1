from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# from games.models import Game

# Create your views here.

def home_view(request:HttpRequest):

    #get all games

    return render(request, 'main/index.html')