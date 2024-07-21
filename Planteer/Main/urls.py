from . import views
from django.urls import path



app_name = 'Main'

urlpatterns = [
    path('', views.home, name='home'),
]
