from . import views
from django.urls import path

app_name = 'Plants'

urlpatterns = [
    path('plants/all/', views.plants, name='plants'),
    path('plants/new/', views.add_plant, name='add_plant'),

]
