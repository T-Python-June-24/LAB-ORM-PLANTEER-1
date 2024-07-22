from django.urls import path
from . import views


app_name = "plant"

urlpatterns =[
    path('add/plant', views.createPlant_view, name= "addPlant.html"),
    path('delete/plant', views.deletePlant_view, name= "deletePlant.html"),
    path('update/plant', views.updatePlant_view, name= "updatePlant.html"),
]