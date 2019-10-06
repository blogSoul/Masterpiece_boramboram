from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import Mainscreen.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Mainscreen.views.home, name='home'),
    
   
    
    path('servicecenter/', include('servicecenter.urls')),
    path('accounts/', include('accounts.urls')),
    path('mypage/', include('mypage.urls')),
    path('designer/', include('designer.urls')),

    path('photo/', include('photo.urls')),
]
