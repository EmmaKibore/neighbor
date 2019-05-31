from django.shortcuts import render,redirect
from django.http import HttpResponse


def home(request):
    profile = Profile.objects.all() 
    businesses = Businesses.objects.all()

    return render(request, 'home.html', {"profile":profile, "businesses":businesses})