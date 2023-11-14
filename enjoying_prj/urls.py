from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('community/', include('community.urls')),
    path('landing/', include('landing.urls')),
    path('', include('landing.urls')),
    path('level/', include('level.urls')),
    path('contactus/', include('contactus.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)