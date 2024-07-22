from django.urls import path
from . import views


app_name = "main"

urlpatterns =[
    path("/", views.home_view, name="home_view"),
    path("allPlant", views.allPlant_view, name="allPlant_view"),
    path("plantDetail/", views.plantDetail_view, name="plantDetail_view"),
    path("contactUs/", views.contactUs_view, name="contactUs_view"),
    path("contactUsMessages/", views.contactUsMessages_view, name="contactUsMessages_view"),
]