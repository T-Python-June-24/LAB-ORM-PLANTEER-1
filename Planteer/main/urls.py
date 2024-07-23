from django.urls import path
from . import views

app_name = 'main'
urlpatterns =[ path('', views.home_view, name="home_view"),
    path('contact/', views.contact_view, name="contact_view"),
    path('users/messages/', views.users_messages_view, name="users_messages_view"),
    path('search/', views.search_view, name="search_view"),
    path("mode/<mode>/", views.mode_view, name="mode_view"),

]