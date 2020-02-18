from django.shortcuts import render,redirect
from django.conf.urls import url
from . import urls

def index(request):
    return render(request,'index.html')