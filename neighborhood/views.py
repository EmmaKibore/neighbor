from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404


def home(request):   
    return render(request, 'home.html')