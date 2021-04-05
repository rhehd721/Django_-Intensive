# Django
- Project 만들기
    - django-admin startproject <project name>
- Server 실행
    - python3 manage.py runserver <port Num>
- App 만들기
    - python3 manage.py startapp <app name>
- DB
    - python3 manage.py migrate
    - python3 manage.py makemigrations <app name>

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

## 참고 블로그
https://velog.io/@teddybearjung