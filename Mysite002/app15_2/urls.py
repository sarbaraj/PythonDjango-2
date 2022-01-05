from django.urls import path
from app15_2 import views

urlpatterns = [
    path('', views.index), # Display All Records
    path('new', views.display_new_form), # Display New Record
    path('update/', views.update),
    path('delete/', views.delete),
]