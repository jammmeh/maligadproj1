from django.shortcuts import render
from django.http import HttpResponse # import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def help(request):
    return HttpResponse('Test')