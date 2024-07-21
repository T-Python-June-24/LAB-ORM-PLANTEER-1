from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('feedbacks/', views.feedbacks, name='feedbacks'),
]