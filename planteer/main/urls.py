
from django.urls import path
from . import views



app_name = "main"
urlpatterns = [
    
    path("",views.home_view,name="home_view"),
    path("plants/new/",views.add_plant_view,name="add_plant_view"),
    path("plants/all/",views.all_plant_view,name="all_plant_view"),
    path("plants/<plant_id>/detail/",views.plant_detail_view,name="plant_detail_view"),
    path("plants/<plant_id>/update/",views.update_plant_view,name="update_plant_view"),
    path("plants/<plant_id>/delete/",views.delete_plant_view,name="delete_plant_view"),
    path("contact/",views.contact_view,name="contact_view"),
    path("contact/messages/",views.contact_messages_view,name="contact_messages_view"),
    path("plants/search/",views.plant_search_view,name="plant_search_view"),
    path("reivew/<plant_id>",views.add_reivew_view,name="add_reivew_view")

    




    
               
               
               ]