from django.urls import path
from . import views

urlpatterns = [
    path('check_permission', views.check_persmission, name='home'),
   
]
