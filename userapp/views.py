from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login
import random
import string

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            # User authentication successful, login the user
            login(request, user)
            return redirect('home')  # Redirect to home page or any other page after login
        else:
            # User authentication failed, handle the case
            error_message = "Invalid username or password. Please try again."
            return render(request, 'lgform.html', {'error_message': error_message})

    return render(request, 'lgform.html')

def generate_random_password():
    # Generate a random password of length 8 consisting of letters and digits
    password_length = 8
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(password_length))

def form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(username, phone_number, email, password)
        data = MyModel(username=username,
                       phone_number=phone_number,
                       email=email,
                       password=password
                       )
        data.save()
        return render(request, template_name='form.html', context={'data': data})
    return render(request, template_name='form.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         data = Lgform(username=username,
#                       password=password)
#         data .save()
#         return render(request, 'form.html', context={'data': data})
#     return render(request, 'lgform.html')

def email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        return render(request, 'forgot_password.html')
    return render(request, 'email.html')

def forgot_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        print(password)
        return render(request, 'lgform.html')
    return render(request, 'forgot_password.html')
