from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to PageFlip! <a href='/pageflip/about/'>About us</a>")

def about(request):
    return HttpResponse("About us")

