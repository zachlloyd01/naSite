from django.shortcuts import render, redirect
from .models import NewsFeed, password_reset, news_application
from .models import comment_page as comments
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, CommentForm, PasswordForm, NewsApp
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def HomePage(request):
    feed = NewsFeed.objects.all()
    return render(request = request, template_name='home.html', context={'feed': feed,})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, f"New Account Created: {username}")
            login(request, user)
            messages.success(request, f"You are now logged in as {username}")
            return redirect("Home:HomePage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    form = NewUserForm
    return render(request,
                  "register.html",
                   context={"form": form,})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("Home:HomePage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("Home:HomePage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def comment_page(request):
    comment = comments.objects.all()
    return render(request, "forum.html", {"comment": comment})

@login_required(login_url='/login/')
def create_comment(request):
    date = datetime.datetime.now().date()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.save()
            messages.info(request, "Your comment has been submitted!")
            return redirect("Home:comment")
        else:
            messages.error(request, "Fill out the comment field!")
    form = CommentForm()
    return render(request, "createcomment.html", {"form": form, "date": date})

def account_page(request):
    name = request.user
    total = 0
    for i in comments.objects.all().filter(name=request.user):
        total += 1
    return render(request, "account.html", {"name": name, "total": total,})

def password_reset(request):
    if request.method == "POST":
        form = password_reset(request.POST)
        if form.is_valid():
            messages.info(request, "Your password has been successfully reset!")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    form = password_reset
    return render(request, "passwordreset.html", {"form": form,})

def application(request):
    if request.method == "POST":
        form = NewsApp(request.POST)
        if form.is_valid():
            post = form.save()
            post.user = str(request.user)
            post.save()
            messages.info(request, "Application successfully submitted!")
            return redirect("Home:account")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    form = NewsApp
    return render(request, "application.html", {"form": form,})