from django.contrib import admin
from django.urls import path, include
from . import views as v1

urlpatterns = [
    path('', v1.index),
    path('displayform1', v1.index220), # display web form
    path('sendvalue1', v1.index221),
]