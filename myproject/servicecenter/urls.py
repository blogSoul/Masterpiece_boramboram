from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='servicecenter'),
    path('<int:servicecenter_id>/', views.detail, name='detail'),
    path('write/', views.write, name='write'),
    path('create/', views.create, name='create'),
]


