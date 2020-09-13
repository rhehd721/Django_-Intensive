from django.contrib import admin
from django.urls import path, include
import app.urls

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('post', views.PostVireSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
