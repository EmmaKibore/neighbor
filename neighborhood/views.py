from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    profile = Profile.objects.all() 
    businesses = Businesses.objects.all()

    return render(request, 'home.html', {"profile":profile, "businesses":businesses})