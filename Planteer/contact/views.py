from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def contact_view(request:HttpRequest):

    return render(request, 'contact/contact.html' )


def message_view(request:HttpRequest):

    return render(request, 'contact/message.html' )


