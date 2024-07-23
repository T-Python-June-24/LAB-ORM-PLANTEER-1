from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponseBadRequest
from plants.models import Plant
from plants.models import Contact
from datetime import datetime
# Create your views here.

def home_view(request: HttpRequest):
     #get all plants    
    plants = Plant.objects.all()[0:3]
    return render(request, 'main/index.html', {"plants" : plants})

    return render(request, 'main/index.html')

def search_view(request: HttpRequest):
    
    query= request.GET.get("query","")
    plants = Plant.objects.filter(name__contains= query)  
    return render(request, 'main/search.html', {"plants" : plants, 'count':plants.count()})

    return render(request, 'main/index.html')



def contact_view(request:HttpRequest):
    if request.method == "POST":
        new_contact = Contact(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], message=request.POST["message"],created_at=datetime.now())
        new_contact.save()
        return redirect('main:home_view')
    return render(request, "main/contact.html")


def users_messages_view(request: HttpRequest):
     #get all contacts    
    contacts = Contact.objects.all()
    return render(request, 'main/users_messages.html', {"contacts" : contacts})

    return render(request, 'main/index.html')



def mode_view(request:HttpRequest, mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")


    return response
