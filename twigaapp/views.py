from django.shortcuts import render,redirect
from .models import Image,Category,Location
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from .forms import *




# Create your views here.
def index(request):
    return render(request, 'index.html')


def products(request):
    
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'products.html',{'images': images[::-1], 'locations':locations})


@csrf_exempt
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form =CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account was created successfully')
                return redirect('login')
        context = {'form': form}
    return render(request,'registration/register.html',  context)

@csrf_exempt
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username ,password=password)
            if user is not None:   
                login(request, user)
        context={}
        return render(request,'registration/login.html',  context) 

def logoutUser(request):
    logout(request)
    return redirect('login')