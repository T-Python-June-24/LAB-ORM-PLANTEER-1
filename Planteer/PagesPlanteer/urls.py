from django.urls import path
from . import views

app_name='PagesPlanteer'

urlpatterns = [
    path('', views.HomePage , name='HomePage'),
    path('plants/all/' , views.DisplayAll , name='DisplayAll'), 
    path('plants/<plant_id>/detail/', views.detail , name='detail'),
    path('plants/new/' , views.new , name='new'),
    path('plants/<plants_id>/update/' , views.update , name='update'),
    path('plants/<plants_id>/delete/' , views.delete , name='delete'),
]