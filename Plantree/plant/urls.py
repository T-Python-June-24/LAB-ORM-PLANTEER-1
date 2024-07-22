from django.urls import path
from . import views


app_name = "plant"

urlpatterns =[
    path('', views.home_view, name= "home_view"),



]