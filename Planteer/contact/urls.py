from django.urls import path
from . import views


app_name = "contact"

urlpatterns = [

    path("contact/", views.contact_view, name="contact_view"),
    path("contact/message", views.message_view, name="message_view"),

]