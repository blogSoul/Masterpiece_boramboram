from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import Mainscreen.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Mainscreen.views.home, name='home'),
    path('servicecenter/', include('servicecenter.urls')),
    path('accounts/', include('accounts.urls')),
    path('mypage/', include('mypage.urls')),
    path('designer/', include('designer.urls')),
    path('request/', include('request.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
