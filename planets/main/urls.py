from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('plants/', views.plants, name='plants'),
    path('light/', views.light, name='light'),
    path('dark/', views.dark, name='dark'),
]