from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from authentication.forms import *
# Create your views here.






def signup(request):
    if request.method == 'POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = SignUpForm()
    return render(request, 'home.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # User is authenticated, log them in.
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')  # Redirect to the home page or any desired URL after login
        else:
            messages.error(request, 'Login failed. Please check your credentials.')
    
    return redirect('home')  # Redirect to the home page or any desired URL after login
def home(request):
    form=SignUpForm()
    
    return render(request,'home.html',{'form':form})