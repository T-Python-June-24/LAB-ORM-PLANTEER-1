from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.
def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(first_name=first_name, last_name=last_name, email=email, message=message)
        contact.save()
        return redirect('feedback:feedbacks')
    return render(request, 'feedback/contact.html')

def feedbacks(request):
    contacts = Contact.objects.all()
    return render(request, 'feedback/feedbacks.html', {'contacts': contacts})