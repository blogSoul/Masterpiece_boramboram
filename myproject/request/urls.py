from django.urls import path
from . import views

urlpatterns = [
    path('', views.requesthome, name='requesthome'),
    path('explain', views.explain, name='explain'),
]