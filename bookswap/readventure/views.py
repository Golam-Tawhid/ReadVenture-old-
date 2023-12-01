from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm,Addbooksform
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Books

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['login_success'] = True
            return redirect('home')
        else:
            return render(request, 'readventure/sign_in.html', {'error_message': 'Invalid login credentials'})
        
    return render(request, 'readventure/sign_in.html')

def home(request):
    if request.session.get('login_success'):
        # del request.session['login_success']
        return render(request, 'readventure/home.html')
    else:
        return redirect('sign_in')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    
    return render(request, 'readventure/sign_up.html', {'form': form})

@login_required
def addbooks(request):
    if request.method == 'POST':
        form = Addbooksform(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            book = form.save(commit=False)
            book.owner = request.user 
            book.save()
            return redirect('mybooks')
        else:
            print("Form is not valid")
            print(form.errors)           
    else:
        form = Addbooksform()
    
    return render(request, 'readventure/addbooks.html', {'form': form})

def sign_up(request):
    return render(request, 'readventure/sign_up.html')

@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'readventure/profile.html', context)

def mybooks(request):
    # Assuming you want to render a template called 'my_books.html'
    # You can pass any necessary context data to this template
    context = {
        'books': Books.objects.all(),  # Assuming Book is a model representing books
        # Other context data...
    }
    return render(request, 'readventure/mybooks.html', context)

def wishlist(request):
    context = {
        'books': Books.objects.all(),
    }
    return render(request, 'readventure/wishlist.html', context)

def borrowed(request):
    context = {
        'books': Books.objects.all(),
    }
    return render(request, 'readventure/borrowed.html', context)