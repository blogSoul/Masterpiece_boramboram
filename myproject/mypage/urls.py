from django.urls import path
from . import views

urlpatterns = [
    path('myinform/', views.myinform, name='myinform'),
    path('myorder/', views.myorder, name='myorder'),
]