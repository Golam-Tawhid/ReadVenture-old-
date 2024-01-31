from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .forms import SignUpForm,Addbooksform, UpdateUserForm
from .models import Books, User, Exchange_info

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'readventure/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('sign_in')

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
    
    background_image = 'peakpx.jpg'
    context = {
        'form': form,
        'background_image': background_image,
    }
    
    return render(request, 'readventure/addbooks.html', context)

def add_to_wishlist(request, book_id):
    if request.method == 'POST':
        book = Books.objects.get(book_id=book_id)
        User.objects.add_to_wishlist(request.user, book)
        return redirect('bookinfo', book_id=book_id)
    else:
        print("Book cannot be added to wishlist")

    return render(request, 'home.html', {'book_id': book_id})

def bookinfo(request, book_id):
    book = get_object_or_404(Books, book_id=book_id)
    background_image = 'img3.jpeg'
    context = {
        'book' : book,
        'background_image' : background_image,
    }
    return render(request, 'readventure/bookinfo.html', context)

def borrowed(request):
    background_image = 'o.jpg'
    context = {
        'books': Books.objects.all(),
        'background_image' : background_image,
    }
    return render(request, 'readventure/borrowed.html', context)

def custom_logout(request):
    logout(request)
    return redirect('sign_in')

def home(request):
    background_image = 'home.jpg'
    if request.session.get('login_success'):
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

        return render(request, 'readventure/home.html', {'background_image' : background_image})
    else:
        return redirect('sign_in')

def mybooks(request):
    background_image = 'j.jpg'
    user_books = Books.objects.filter(owner=request.user)
    for book in user_books:
        print(f'Book ID: {book.book_id}, Title: {book.title}, Owner: {book.owner}')
    context = {
       'background_image' : background_image,
       'user_book' : user_books,
   }
    return render(request, 'readventure/mybooks.html', context)

@login_required
def profile(request):
    user = request.user
    background_image = 'm.jpg'
    context = {
        'user': user,
        'background_image' : background_image,
        }
    return render(request, 'readventure/profile.html', context)

def requests(request):
    background_image = 'img22.jpg'
    incoming_requests = Exchange_info.objects.filter(owner=request.user, status='pending')
    accepted_requests = Exchange_info.objects.filter(owner=request.user, status='accepted')
    outgoing_requests = Exchange_info.objects.filter(borrower=request.user, status='pending')

    context = {
        'incoming_requests': incoming_requests,
        'outgoing_requests': outgoing_requests,
        'accepted_requests': accepted_requests,
        'background_image': background_image,
    }

    return render(request, 'readventure/requests.html', context)

def remove_book(request, book_id):
    try:
        
        book = get_object_or_404(Books, book_id=book_id, owner=request.user)
        book.delete()
    except Books.DoesNotExist:
        raise Http404("Book does not exist")
    return redirect('mybooks')

def remove_from_wishlist(request, book_id):
    book = get_object_or_404(Books, book_id=book_id)
    request.user.wishlist.remove(book)

    return redirect('wishlist')  

def request_to_borrow(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Books, book_id=book_id)
        
        # Assuming the owner is a field in the Books model
        owner = book.owner
        
        # Create Exchange_info instance with owner and borrower
        Exchange_info.objects.create(book=book, owner=owner, borrower=request.user)  # Assuming authenticated user
        return redirect('requests')
    
    else:
        print("Book cannot be added")
    
    return render(request, 'readventure/home.html', {'book_id': book_id})

# def request_to_borrow(request, book_id):
#     if request.method == 'POST':
#         book = Books.objects.get(book_id=book_id)
#         owner = book.owner
#         Exchange_info.objects.create(book=book, borrower=request.user)  # Assuming authenticated user
#         return redirect('bookinfo', book_id=book_id)
    
#     else:
#         print("Book cannot be added")
#     return render(request, 'readventure/home.html', {'book_id': book_id})

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
           messages.error(request, 'Invalid login credentials')
        
    return render(request, 'readventure/sign_in.html')

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
    
    errors = form.errors.values() if form.errors else None

    return render(request, 'readventure/sign_up.html', {'form': form, 'errors': errors})

def sign_up(request):
    return render(request, 'readventure/sign_up.html')


# def toggle_availability(request, book_id):
#     book = get_object_or_404(Books, book_id=book_id, owner=request.user)

#     # Retrieve or create the Availability record for the book
#     availability, created = Availability.objects.get_or_create(book_id=book_id)

#     # Toggle the availability status
#     availability.status = 'Unavailable' if availability.status == 'Available' else 'Available'
#     availability.save()

#     # Return the updated availability status in the JsonResponse
#     return JsonResponse({'availability': availability.status})

def update_user(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print(form.errors)
    else:
        form = UpdateUserForm(instance=request.user)
    
    return render(request, 'readventure/updateprofile.html', {'form': form})

def wishlist(request):
    background_image = 'booklist.jpg'
    context = {
        'books': Books.objects.all(),
        'background_image' : background_image,
    }
    user_wishlist = request.user.wishlist.all()
    return render(request, 'readventure/wishlist.html', context)

#----------------------------------------------------------------------------
def ignore_request(request, exchange_id):
    exchange_info = get_object_or_404(Exchange_info, exchange_id=exchange_id)
    exchange_info.status = 'ignored'
    exchange_info.save()
    return redirect('requests')

def accept_request(request, exchange_id):
    exchange_info = get_object_or_404(Exchange_info, exchange_id=exchange_id)
    exchange_info.status = 'accepted'
    exchange_info.save()
    return redirect('requests')

def cancel_request(request, exchange_id):
    exchange_request = get_object_or_404(Exchange_info, exchange_id=exchange_id)
    # Perform logic for canceling the request (e.g., delete the request)
    exchange_request.delete()
    return redirect('requests')