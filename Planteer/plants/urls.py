from django.urls import path
from . import views


app_name = "plants"

urlpatterns = [

    path("plants/new/", views.add_plants, name="add_plants"),
    # path("plants/all/", views.create_game_view, name="create_game_view"),
    # path("plants/<plant_id>/detail/", views.create_game_view, name="create_game_view"),
    # path("plants/<plant_id>/update/", views.create_game_view, name="create_game_view"),
    # path("plants/<plant_id>/delete/", views.create_game_view, name="create_game_view"),

]