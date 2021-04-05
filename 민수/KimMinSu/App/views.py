from django.shortcuts import render, redirect, get_object_or_404
# from .models import Item, Order, Store

def index(request):
    return render (request, './html/index.html')