from django.urls import path
from . import views


app_name = "plants"

urlpatterns = [
    path("plant/", views.plant_list_view , name="plant_list_view"),
    path("contact/", views.contact_list_view , name="contact_list_view"),
    path("all/", views.all_plant_view , name="ll_plant_view"),
    path("detail/<plant_id>/" , views.plant_detail_view , name= "plant_detail_view"),
    path("update/<plant_id>/" , views.plant_update_view , name= "plant_update_view"),
    path("delete/<plant_id>/" , views.plant_delete_view , name= "plant_delete_view")




    
]