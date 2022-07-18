from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['pass']

        # chack for password mismatch
        if password != password2:
            messages.info(request, 'password mismatch')
            return redirect('signup')
        else:
            # chack for existing user
            user = User.objects.filter(email=email).exists()
            if user is not None:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                messages.info(request, 'user created successfully')
                return redirect('signin')
            else:
                messages.info(request, 'user already exist')
                return redirect('signup')

    return render(request, 'core/signup.html')


def signOut(request):
    logout(request)
    return redirect('/')


def signIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('signin')
    return render(request, 'core/signin.html')


def about(request):
    return render(request, 'core/about.html')


def blog(request):
    return render(request, 'core/blog.html')


def contact(request):
    return render(request, 'core/contact.html')
