from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from store.models import Customer 
from django.contrib import messages 
# Create your views here.
def login(request):
    if request.method=='GET':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        customer = authenticate(request,username=email,password=password)
        if customer is not None:
            login(request,customer)
            return render(request,'index.html')
        else:
            messages.error(request,'Sorry ! Wrong username or password') 

def logout(request):
    logout(request)
    messages.success(request,'Successfully signed out !')
    return redirect('main')
def register(request):
    if request.method=='POST':
        name = request.POST.get('UserName')
        email = request.POST.get('Email')
        password1 = request.POST.get('Password1')
        password2 = request.POST.get('Password2')
        #creating customer 
        customer = User.objects.create_User(name=name,email=email,password=password1)
        customer.save()
        messages.success(request,'Your account created successfully !')
        return redirect('login')