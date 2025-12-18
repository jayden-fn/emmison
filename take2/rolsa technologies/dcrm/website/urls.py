from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculate/', views.calculate, name='calculate'),
    path('booking/', views.booking, name='booking'),
]

