# portfolio_blog/blog/views.py

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world. Welcome to the blog index.")