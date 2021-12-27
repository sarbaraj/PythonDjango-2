from django.contrib import admin
from django.urls import path, include
from . import views as v1

urlpatterns = [
    path('', v1.index),
    path('new', v1.new),
    path('receivenew', v1.receivenew),
    path('displayedit', v1.displayedit),
    path('receiveedit', v1.receiveedit),
    path('displaydelete', v1.displaydelete),
]