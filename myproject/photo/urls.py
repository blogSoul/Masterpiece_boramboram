from django.urls import path
from django.views.generic.detail import DetailView

from .views import *
from .models import Photo

app_name ='photo'
# namespace - 템플릿에서 url템플릿 태그를 사용할 때 [app_name:URL패턴이름] 형태로 사용



urlpatterns = [
    path('category/all', photo_list, name='category_all'),
    path('category/illust/', photo_list, name='category'),

    path('detail/<int:pk>/', DetailView.as_view(model=Photo, template_name='Mainscreen/detail.html'), name ='Mainscreen_detail'),
    path('commission/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]
