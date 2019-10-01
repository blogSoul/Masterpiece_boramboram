from django.urls import path
from . import views

urlpatterns = [
    path('designerhome/', views.designerhome, name='designerhome'),
    path('detail/', views.detail, name='detail'),
]