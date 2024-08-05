from django.urls import path
from . import views



app_name = "plant"

urlpatterns =[
    path('listAll/plant', views.listAllPlant_view, name= "listAllPlant_view"),
    path('add/plant', views.createPlant_view, name= "createPlant_view"),
    path('update/<int:plant_id>/', views.updatePlant_view, name= "updatePlant_view"),
    path('delete/<plant_id>/', views.deletePlant_view, name='deletePlant_view'),
]