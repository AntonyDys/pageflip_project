from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from pageflip.forms import UserForm, UserProfileForm


def index(request):

    context_dict = {}
    context_dict['boldmessage'] = 'This months genre: Sci-fi!'

    response = render(request, 'pageflip/index.html', context=context_dict)

    return response

def about(request):

    context_dict = {}
    context_dict ['boldmessage']= 'PageFlip is an online home for all your reading needs'

    response = render(request, 'pageflip/about.html', context=context_dict)
    return response

