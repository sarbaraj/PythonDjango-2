from django.contrib import admin
from django.urls import path
from app4 import views

urlpatterns = [
    path('', views.index),
    path('contact', views.contact),
    path('cookbook/', views.cookbook),
    path('cuisine/', views.cuisine),
    path('wine/', views.wine),
]
