from django.urls import path
from . import views


app_name = "plants"

urlpatterns = [
    path("create/", views.create_plant_view, name="create_plant_view"),
    path("all/", views.all_plants_view, name="all_plants_view"),
    path("detail/<plant_id>", views.plant_detail_view, name="plant_detail_view"),
    path("update/<plant_id>/", views.plant_update_view, name="plant_update_view"),
    path("delete/<plant_id>/", views.plant_delete_view, name="plant_delete_view"),
    path("search/", views.plant_search_view, name='plant_search_view'),
]