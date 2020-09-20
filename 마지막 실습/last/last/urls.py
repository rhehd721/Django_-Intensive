from django.contrib import admin
from django.urls import path, include
from app import urls
from rest_framework import urls

#파일업로드
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

#파일업로드
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
