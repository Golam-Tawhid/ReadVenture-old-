from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from .models import User

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['login_success'] = True
            return redirect('home')  # Redirect to the home page
        else:
            # Handle invalid login credentials
            return render(request, 'readventure/sign_in.html', {'error_message': 'Invalid login credentials'})
        
    return render(request, 'readventure/sign_in.html')

def home(request):
    if request.session.get('login_success'):
        # del request.session['login_success']  # Remove the session variable to avoid showing the message on page refresh
        return render(request, 'readventure/home.html')
    else:
        # Redirect to the login page if there's no successful login session
        return redirect('sign_in')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profilepic')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    
    return render(request, 'readventure/sign_up.html', {'form': form})

def sign_up(request):
    return render(request, 'readventure/sign_up.html')

def profile(request):
    return render(request, 'readventure/profile.html')

def profilepic(request):
    return render(request, 'readventure/profilepic.html')