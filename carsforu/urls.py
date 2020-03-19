from django.urls import path
from . import views

 

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_it', views.submit_it, name='submit_it'),
]

