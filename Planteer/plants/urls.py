from django.urls import path
from . import views


app_name = "plants"

urlpatterns = [
    path('all/', views.all_plants, name="all_plants"),
    path('<plant_id>/detail/', views.plant_detail , name="plant_detail"),
    path('new/', views.add_plant, name="add_plant"),
    # path('<plant_id>/update/', views.update_plant, name="update_plant"),
    path('<plant_id>/delete/', views.delete_plant, name="delete_plant"),

]   