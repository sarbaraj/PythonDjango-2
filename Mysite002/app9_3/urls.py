from django.urls import path
from . import views

urlpatterns = [
    path('emp/', views.emp), # insert news
    path('show',views.show), # display all
    path('edit/<int:id>', views.edit), # display for edit
    path('update/<int:id>', views.update), # update record
    path('delete/<int:id>', views.destroy), # delete record
]

