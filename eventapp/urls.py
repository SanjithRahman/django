from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('about/<int:pk>',views.about,name="about"),
   path('event-details',views.eventdetails,name="eventdetail")
]
