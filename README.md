# Django
- Project 만들기
    - django-admin startproject mysite
- Server 실행
    - python3 manage.py runserver 8080
- App 만들기
    - python3 manage.py startapp polls
- DB
    - python3 manage.py migrate

## urls.py
- project/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('App.urls')),
    path('admin/', admin.site.urls),
]
```
- App/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
- views.py
```python
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

## templates

## setting.py
```python
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'
```

## Bootstrap
https://getbootstrap.kr/