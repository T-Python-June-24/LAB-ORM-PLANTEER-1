from django.urls import path
from . import views

app_name = 'plants'

urlpatterns = [
    path('all/', views.all, name='all'),
    path('<plant_id>/detail/', views.details, name='details'),
    path('new/', views.add, name='add'),
    path('<plant_id>/update/', views.update, name='update'),

]
