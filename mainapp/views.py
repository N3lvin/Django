from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from .models import User
from .models import Songs
from .models import Teamresults
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
# Create your views here.
def homepage(request):
    return HttpResponse("Hello")

def aboutus(request):
    return HttpResponse("Deadpool")

def contactpage(request):
    return render(request,"contact.html")
def pricingpage(request):
    price=3000
    if request.method=="POST":
        typedname=request.POST.get("firstname")
        print("python has received"+typedname)
        typednumber=request.POST.get("number")
        print("python has received" +typednumber)
    return render(request, "pricing.html",{"myprice":price})

def Login(request):
    if request.method=="POST":
        typedname=request.POST.get("username")
        print("python has received"+typedname)
        typedpassword=request.POST.get("password")
        print("python has received" +typedpassword)
        typedEmail=request.POST.get("Email")
        print("python has received"+typedEmail)
        new_user=User(username=typedname,password=typedpassword,email=typedEmail)
        new_user.save()
    return render(request,"login.html")
def fetch_allusers(request):
    allusers=User.objects.all()
    return render(request,"fetch_alluser.html",{"allmyusers":allusers})
def create_songs(request:HttpRequest):
    if request.method=="POST":
        typedname=request.POST.get("name")
        typedartist=request.POST.get("artist")
        typedlisteners=request.POST.get("listeners")
        typedlyrics=request.POST.get("lyrics")
        new_Songs=Songs(name=typedname,artist=typedartist,listeners=typedlisteners,lyrics=typedlyrics)
        new_Songs.save()
    return render(request,"create_songs.html" )  
def fetch_allsongs(request):
    allsongs=Songs.objects.all()
    return render(request, "fetch_allsongs.html",{"allsongs":allsongs})  
def fetch_onesong(request,id):
    one_song=Songs.objects.get(pk=id)
    return render(request,"fetch_onesong.html",{"one_song":one_song})
def fetch_oneuser(request,id):
    one_user=User.objects.get(pk=id)
    return render(request,"fetch_oneuser.html",{"one_user":one_user})
def edit_song(request,id):
    one_song=Songs.objects.get(pk=id)
    if request.method=="POST":
        typedname=request.POST.get("name")
        typedartist=request.POST.get("artist")
        typedlisteners=request.POST.get("listeners")
        typedlyrics=request.POST.get("lyrics")
        one_song.name=typedname
        one_song.artist=typedartist
        one_song.listeners=typedlisteners
        one_song.lyrics=typedlyrics
        one_song.save()

    return render(request,"edit_song.html",{"one_song":one_song})
def edit_user(request,id):
    one_user=User.objects.get(pk=id)
    if request.method=="POST":
        typedname=request.POST.get("username")
        typedemail=request.POST.get("Email")
        typedpassword=request.POST.get("password")
        one_user.username=typedname
        one_user.email=typedemail
        one_user.password=typedpassword
        one_user.save()
    return render(request,"edit_user.html",{"one_user":one_user})
def delete_user(request,id):
    one_user=User.objects.get(pk=id)
    one_user.delete()
    return redirect("homepage")
def delete_onesong(request,id):
    one_song=Songs.objects.get(pk=id)
    one_song.delete()
    return redirect("aboutus")
def create_record(request:HttpRequest):
    if request.method=="POST":
        typedteam=request.POST.get("team")
        typedwins=request.POST.get("wins")
        typeddraws=request.POST.get("draws")
        
        new_Teamresults=Teamresults(team=typedteam,wins=typedwins,draws=typeddraws)
        new_Teamresults.save()

def sign_in(request:HttpRequest):
    if request.method=="POST":
        typedusername=request.POST.get("username")
        typedpassword=request.POST.get("password")
        print(typedpassword)
        print(typedusername)

        result = authenticate(username =typedusername,password =typedpassword)
        if result ==None:
            return HttpResponse("That account doesn't exist")
        else:
            login(request,result)
            return HttpResponse("Welcome")


    return render(request,"sign_in.html")
def sign_up(request:HttpRequest):
    if request.method=="POST":
        typedEmail=request.POST.get("Email")
        typedpassword=make_password(request.POST.get("password"))
        typedFirstname=request.POST.get("Firstname")
        typedSecondname=request.POST.get("Secondname")
        typedusername=request.POST.get("username")
        print(typedEmail)
        print(typedpassword)
        print(typedFirstname)
        print(typedSecondname)
        print(typedusername)

        new_user=User(username=typedusername,password=typedpassword,email=typedEmail,first_name=typedFirstname,last_name=typedSecondname)
        new_user.save()
         
    return render(request,"sign_up.html")