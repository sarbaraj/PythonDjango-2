from django.urls import path
from . import views # 1

urlpatterns = [
    path('model_crud', views.crud),
]