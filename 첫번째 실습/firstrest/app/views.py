from rest_framework import viewsets
from django.shortcuts import render, redirect
from .models import Post
from .serializer import PostSerializer


# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    