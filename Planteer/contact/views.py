from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact/contact.html')


def messages(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact/messages.html')