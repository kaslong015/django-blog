from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import *

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


def settings(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        print(request.FILES.get('image'))
        if request.FILES.get('image') == None:
            image = profile.image
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']

            profile.image = image
            profile.firstname = firstname
            profile.lastname = lastname

            profile.save()
            messages.info(request, 'profile updated successfully')
            # return redirect('settings')
        else:

            image = request.FILES.get('image')
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']

            profile.image = image
            profile.firstname = firstname
            profile.lastname = lastname
            profile.save()
            messages.info(request, 'profile updated successfully')
            # return redirect('settings')

    return render(request, 'core/settings.html', {'profile': profile, })


def blog(request):
    blog_post = Post.objects.all().order_by('created_at').reverse()
    context = {
        'blog_post': blog_post
    }
    return render(request, 'core/blog.html', context)


def post_detail(request, pk):
    postDetails = Post.objects.get(id=pk)
    related_post = Post.objects.filter(user=postDetails.user)[:3:-1]

    new_comment = Comment.objects.filter(post=postDetails)

    if request.method == 'POST':
        comment = request.POST['comment']
        user = request.user
        post = postDetails

        new_comment = Comment.objects.create(
            comment=comment, user=user, post=post)
        new_comment.save()

    context = {
        'post_details': postDetails,
        'related_post': related_post,
        'comments': new_comment,
        'comment_count': new_comment.count()
    }
    return render(request, 'core/blog-single.html', context)


def contact(request):
    return render(request, 'core/contact.html')
