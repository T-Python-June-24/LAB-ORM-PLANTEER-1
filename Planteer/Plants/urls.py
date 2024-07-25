from django.urls import path
from . import views

app_name = 'Plants'

urlpatterns = [
    path('plants/all/', views.plants, name='plants'),
    path('plants/new/', views.add_plant, name='add_plant'),
    path('plants/<int:plant_id>/detail/', views.plant_detail, name='plant_detail'),
    path('plants/<int:plant_id>/update/', views.update_plant, name='update_plant'),
    path('plants/<int:plant_id>/delete/', views.delete_plant, name='delete_plant'),
    path('plants/search/', views.search_plant, name='search_plant'),
    path('review/<int:plant_id>/add/', views.users_review, name='users_review'),
    path('review/reviews/', views.display_reviews, name='display_reviews'),  # Fixed typo here

]
