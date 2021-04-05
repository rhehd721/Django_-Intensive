from django.shortcuts import render, redirect, get_object_or_404
from .models import Board

def index(request):
    return render (request, './html/index.html')

def board(request):
    boards= Board.objects.all().order_by('-id')
    return render (request, './html/board.html', {"boards":boards})