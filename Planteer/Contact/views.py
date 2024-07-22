from django.shortcuts import render , redirect
from django.http import HttpRequest
from .models import Contact

# Create your views here.
def contact(request:HttpRequest):
    if request.method == "POST":
        save_message = Contact(first_name = request.POST['first_name'] , last_name = request.POST['last_name'] , email = request.POST['email'] , message = request.POST['message'])
        save_message.save()
    return render(request , 'pages/contact.html')

def messages(request:HttpRequest):
    messages=Contact.objects.all()
    return render(request , 'pages/messages.html',{'message':messages})
