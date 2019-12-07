from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("welcome back deepshikha")

def new_pro(request):
    return HttpResponse("Hurry ....new product arrives")
