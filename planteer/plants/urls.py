from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('plants/all/', views.all_plants, name='all_plants'),
    path('plants/<int:plant_id>/detail/', views.plant_detail, name='plant_detail'),
    path('plants/new/', views.new_plant, name='new_plant'),
    path('plants/<int:plant_id>/update/', views.update_plant, name='update_plant'),
    path('plants/<int:plant_id>/delete/', views.delete_plant, name='delete_plant'),
    path('contact/', views.contact, name='contact'),
    path('contact/messages/', views.contact_messages, name='contact_messages'),
]
