from . import views
from django.urls import path


app_name = "plants"


urlpatterns = [
    path('plants/all/', views.all_plants, name='all_plants'),
    path("new/", views.create_plant, name="new_plant"),
    path("detail/<plant_id>/", views.plant_detail, name="plant_detail"),
    path("update/<plant_id>/", views.plant_update, name="plant_update"),
    path("delete/<plant_id>/", views.plant_delete, name="plant_delete"),
    path('search/', views.search, name='search'),
]