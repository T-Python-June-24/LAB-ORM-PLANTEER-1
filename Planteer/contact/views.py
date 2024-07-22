from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact



def contact_view(request:HttpRequest):

    if request.method == 'POST':
        
        contact = Contact(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], message=request.POST['message'])
        contact.save()
        return redirect('contact:contact_view')

    return render(request, 'contact/contact.html' )


def message_view(request:HttpRequest):

    contacts = Contact.objects.all()

    return render(request, 'contact/message.html', {'contacts': contacts})
