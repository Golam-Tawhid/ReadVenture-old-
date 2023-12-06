from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import SignUpForm,Addbooksform
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Books, User, Receipt

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
    # Check if the user is logged in
    if request.session.get('login_success'):
        # Check if it's a POST request (form submission)
        if request.method == 'POST':
            search_query = request.POST.get('search_query', '')
            search_type = request.POST.get('search_type', 'all')

            if search_type == 'all':
                books = Books.objects.filter(title__icontains=search_query) | Books.objects.filter(author__icontains=search_query)
            elif search_type == 'author':
                books = Books.objects.filter(author__icontains=search_query)
            elif search_type == 'title':
                books = Books.objects.filter(title__icontains=search_query)
            else:
                books = Books.objects.all()

            return render(request, 'readventure/home.html', {'books': books, 'search_query': search_query, 'search_type': search_type})

        return render(request, 'readventure/home.html')

    # If not logged in, redirect to the sign-in page
    else:
        return redirect('sign_in')
    
def bookinfo(request, book_id):
    book = get_object_or_404(Books, book_id=book_id)
    return render(request, 'readventure/bookinfo.html', {'book': book})

def add_to_wishlist(request, book_id):
    if request.method == 'POST':
        book = Books.objects.get(book_id=book_id)
        # Assuming authenticated user
        User.objects.add_to_wishlist(request.user, book)
        return redirect('bookinfo', book_id=book_id)
    else:
        print("Book cannot be added to wishlist")

    return render(request, 'home.html', {'book_id': book_id})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
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
    user_books = Books.objects.filter(owner=request.user)
    return render(request, 'readventure/mybooks.html', {'user_books': user_books})

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

def requests(request):
    ############ DUNNO WHAT TO WRITE ######################