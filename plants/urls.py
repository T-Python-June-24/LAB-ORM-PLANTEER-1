from django.urls import path
from . import views

app_name = 'plants'

urlpatterns = [
    path('all/', views.all_plants, name='all_plants'),
    path('details/<int:id>/', views.plant_details, name='plant_details'),
    path('new/', views.new_plant, name='new_plant'),
    path('update/<int:id>/', views.update_plant, name='update_plant'),
    path('delete/<int:id>/', views.delete_plant, name='delete_plant'),
    path('search/', views.search_plants, name='search_plants'),
]
