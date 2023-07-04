from django.shortcuts import render,HttpResponse,redirect
from .models import room
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .forms import BookingForm,ContactForm
# Create your views here.

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("invalid user name")

    return render(request,'login.html')
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("incorrect password")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')

@login_required(login_url='login')
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        cform=ContactForm(request.POST)
        if cform.is_valid():
            cform.save()
            return render(request,'confirmation.html')
    cform=ContactForm()
    return render(request,'contact.html',{'form':cform})
def service(request):
    return render(request,'services.html')
def rooms(request):
    rooms=room.objects.all()
    return render(request,'rooms.html',{'room':rooms})
def booking(request):
    if request.method == "POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm()
    return render(request,'booking.html',{'form':form})

def viewbooking(request):
    return render(request,'viewbooking.html')
def LogoutPage(request):
    logout(request)
    return redirect('login')
