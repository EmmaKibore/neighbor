from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):  
    neighborhood = neighborhood.objects.all() 
    return render(request, 'home.html',{{"neighborhood":neighborhood}})

def profile(request):
    current_user = request.user
    neighborhood = Neighbourhood.objects.all()
    profile = Profile.objects.all()

    
    return render(request, 'profile.html', {"profile":profile,"neighborhood":neighborhood})   

def edit_profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    if request.method == 'POST':
        signup_form = EditForm(request.POST, request.FILES,instance=request.user.profile) 
        if signup_form.is_valid():
            signup_form.save()
            return redirect('profile')
    else:
        signup_form =EditForm() 
        
    return render(request, 'edit_profile.html', {"form":signup_form,"profile":profile})
    
@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.objects.filter(name=search_term)
        message = f"{search_term}"
        profiles=  Profile.objects.all( )
      
        return render(request, 'search.html',{"message":message,"business": searched_businesses,'profiles':profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def neighborhood(request,id):
    date = dt.date.today()
    post=Neighbourhood.objects.get(id=id)
    brushs = Post.objects.filter(neighbourhood=post)
    business = Business.objects.filter(neighbourhood=post)
    return render(request,'each_hood.html',{"post":post,"date":date,"brushs":brushs, "business":business})


def new_post(request,id):
    date = dt.date.today()
    hood=Neighbourhood.objects.get(id=id)
    posts = Post.objects.filter(neighbourhood=hood)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.profile = profile
            post.neighbourhood = hood
            post.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request,'new_post.html',{"form":form,"posts":posts,"hood":hood,  "date":date})

