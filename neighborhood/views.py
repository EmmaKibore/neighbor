from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404


def home(request):  
    neighborhood = neighborhood.objects.all() 
    return render(request, 'home.html',{{"neighborhood":neighborhood}})

def profile(request):
    current_user = request.current_user
    profile = profile.objects.get(user=current_user.id)
    neighborhood = Neighborhood.objects.all()
    return render(request, 'profile/profile.html', {"profile":profile,"neighborhood":neighborhood})    