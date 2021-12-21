from django.contrib import admin
from django.urls import path, include
from . import views as v1

urlpatterns = [
    path('sendvalue1', v1.index21),
    path('sendvalue2', v1.index22),
    path('displayform', v1.index23),
    path('sendvalue3', v1.index24),
    path('sendvalue4', v1.index25),
    path('sendvalue5/<n1>/<n2>/', v1.index26),
    path('loadstatic/', v1.index27),
    path('bootstrap1/', v1.index28),
    path('bootstrap2/', v1.index29),
]