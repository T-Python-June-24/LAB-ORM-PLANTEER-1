from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact



# Create your views here.
def display_contact_messages(request:HttpResponse):
    Messages = Contact.objects.all()
    return render(request, 'Contact/display_messages.html',{'Messages':Messages})


def send_contact_message(request:HttpResponse):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            message = request.POST['message']
            contact = Contact(
                first_name=first_name,
                last_name=last_name,
                email=email,
                message=message
            )
            contact.save()
            messages.success(request, 'Plant added successfully!')
        except MultiValueDictKeyError as e:
            messages.error(request, f'Missing field: {str(e)}')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
    return render(request, 'Contact/contact.html')