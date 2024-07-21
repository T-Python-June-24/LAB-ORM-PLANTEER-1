from . import views
from django.urls import path


app_name = 'Contact'

urlpatterns = [
    path('contact/', views.send_contact_message, name='send_contact_message'),
    path('contact/messages/', views.display_contact_messages, name='display_contact_messages'),
    path('contact/thanks/', views.thanks, name='thanks'),
    path('contact/add_plant/thanks', views.thanks_add_plant, name='thanks_add_plant'),
]
