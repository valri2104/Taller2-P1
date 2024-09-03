from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies_list, name='movies_list'),
    # otras URLs
]

