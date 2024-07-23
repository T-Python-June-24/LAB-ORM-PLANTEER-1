from django.urls import path
from . import views


app_name = "plants"

urlpatterns = [

    path("new/", views.add_plants, name="add_plants"),
    path("all/", views.all_view, name="all_view"),
    path("<plant_id>/detail/", views.detail_view, name="detail_view"),
    path("<plant_id>/update/", views.update_plant, name="update_plant"),
    path("<plant_id>/delete/", views.delete_plant, name="delete_plant"),
    path("search/", views.search_plants, name="search_plants"),

]