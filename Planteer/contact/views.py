from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from contact.models import Contact

# Create your views here.

def contact_view(request:HttpRequest):
    if request.method == "POST":
        new_contact=Contact(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            message=request.POST["message"],
        )
        new_contact.save()
        return redirect('main:home_view')
    return render(request, "contact/contact_view.html")

def contact_messages(request:HttpRequest):
    contacts=Contact.objects.all()
    return render(request, 'contact/contact_messages.html', {"contacts" : contacts} )



