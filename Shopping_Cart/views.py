from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Django Includes Shopping_cart URLs</h1>')