from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):  
    
    return render(request, 'home.html')

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
    post=Neighborhood.objects.get(id=id)
    brushs = Post.objects.filter(neighborhood=post)
    business = Business.objects.filter(neighborhood=post)
    return render(request,'each_hood.html',{"post":post,"date":date,"brushs":brushs, "business":business})

def neighborhoods(request):
    neighborhoods = Neighbourhood.objects.all()
   
    return render(request,'new_neighborhood.html',{"neighborhoods":neighborhoods})



def new_post(request,id):
    date = dt.date.today()
    hood=Neighborhood.objects.get(id=id)
    posts = Post.objects.filter(neighborhood=hood)
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

def new_business(request,id):
    date = dt.date.today()
    business = Business.objects.filter(neighborhood=neighborhood)
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.profile = request.user.profile
            business.neighborhood = hood
            business.save()
            return redirect('index')
    else:
        form = BusinessForm()
        return render(request,'new_business.html',{"form":form,"business":business,"neighborhood":neighborhood,  "date":date})

