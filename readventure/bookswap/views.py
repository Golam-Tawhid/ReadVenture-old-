# yourappname/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import SignInForm

# def sign_in(request):
#     if request.method == 'POST':
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('dashboard')
#             else:
#                 return render(request, 'bookswap/signin.html', {'form': form, 'error': 'Invalid credentials'})
#     else:
#         form = SignInForm()

#     return render(request, 'bookswap/signin.html', {'form': form})
# yourappname/views.py
def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            # ... (your existing code)
    else:
        form = SignInForm()

    return render(request, 'yourappname/signin.html', {'form': form})
