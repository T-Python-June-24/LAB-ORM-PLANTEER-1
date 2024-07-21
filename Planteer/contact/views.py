from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def contact_view(request:HttpRequest):
    print("initial contact")

# def contact_messages