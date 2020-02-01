from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from home.models import post
from django.contrib.auth.decorators import login_required
from .forms import contactform

# Create your views here.
def signup1(req):
    if req.method=="POST":
       new_user = User.objects.create_user(
           username=req.POST['username'],
           email=req.POST['email'],
           password=req.POST['password'],
           first_name=req.POST['fname'],
           last_name=req.POST['lname']
           )
       return redirect('home:login1')
    else:
        return render(req,'home/index.html')

def login1(req):
    if req.method=="POST":
        user=authenticate(
            username=req.POST['username'],
            password=req.POST['password']
            )
        if user:
            login(req,user) #to allow user to be logged in
            return redirect('home:addpost')
            
        else:
            return HttpResponse("Invalid!!!!")
    
    else:
        return render(req,'home/login.html')

@login_required
def addpost(req):
    if req.method=="POST":
        new_post=post()
        new_post.title=req.POST.get("title")
        new_post.content=req.POST.get("content")
        new_post.posted_by=req.user
        new_post.save()
    return render(req,'home/addpost.html',{'data':'HEllooooooooooo'})

@login_required
def logout1(req):
    logout(req)
    return redirect('home:login')

def index1(req):
    posts=post.objects.all()
    return render(req,'home/index1.html',{'posts':posts})

def posts(req):
    #http://127.0.0.1:8000/posts/?name=sankiii12
    user=User.objects.get(username=req.GET['name'])
    posts=post.objects.filter(posted_by=user)
    
    return render(req,'home/index1.html',{'posts':posts})

def post_id(req,keys):
    #http://127.0.0.1:8000/posts/id/1
    #http://127.0.0.1:8000/posts/id/2
    posts=post.objects.filter(id=keys)
    return render(req,'home/index1.html',{'posts':posts})

    
    


def archive(req):  #MONTHLY AND YEARLY DISPLAYING OF POSTS
    #http://127.0.0.1:8000/archive/monthly/?month=9&&year=2019
    month=req.GET['month']
    year=req.GET['year']
    posts=post.objects.filter(posted_on__month=month,posted_on__year=year)
    return render(req,'home/index1.html',{'posts':posts})

def archive_yearly(req):
    #http://127.0.0.1:8000/archive/yearly/?year=2019
    year=req.GET['year']
    posts=post.objects.filter(posted_on__year=year)
    return render(req,'home/index1.html',{'posts':posts})

def contactus(req):
    if req.method=="POST":
        form=contactform(req.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            print(name)
            return HttpResponse("FORM SUBMISIION SUCCESSFULL")
        else:
            return HttpResponse("INAVLID FORM SUBMISIION")
    else:
        form=contactform()
        return render(req,'home/contactus.html',{'form1':form})