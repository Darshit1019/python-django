from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event_registration/', views.event_registration, name='event_registration'),
    path('participant_registration/', views.participant_registration, name='participant_registration'),
]