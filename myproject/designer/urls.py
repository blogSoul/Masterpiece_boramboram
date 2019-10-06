from django.urls import path
from . import views

urlpatterns = [
    path('designerhome/', views.designerhome, name='designerhome'),
    path('designerhome/<int:Art_id>', views.detail, name='detail'),
]