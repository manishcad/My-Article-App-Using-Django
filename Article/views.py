from django.shortcuts import render, redirect
from .models import Article, Tag, Author
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    author = Author.objects.all().first()

    tags = Tag.objects.all()

    article_2023 = Article.objects.filter(
        created__range=['2023-01-01', "2023-12-31"])

    context = {'tags': tags, 'author': author, "article_2023": article_2023}
    return render(request, 'index.html', context)


def show_article(request, pk):
    article = Article.objects.filter(uid=pk).first()

    tag = article.tags.all().first()
    related_articles = Article.objects.filter(tags=tag)
    context = {"article": article, "related_articles": related_articles}
    return render(request, "Show_article.html", context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect("Home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("Home")
        else:
            messages.warning(request, "Incorrect Username or Password")
            return redirect("Login")
    return render(request, 'login.html')


def logout_page(request):
    print("This is working")
    logout(request)
    return redirect("Home")


def about(request, pk):
    author = Author.objects.filter(uid=pk).first()
    context = {"author": author}
    return render(request, "about.html", context)


def signup(request):
    if request.user.is_authenticated:
        return redirect("Home")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if User.objects.filter(username=username):
            messages.warning(
                request, "User is already Taken try another-one")
            return redirect("Signup")
        if User.objects.filter(email=email):
            messages.warning(
                request, "User is already Taken try another-one")
            return redirect("Signup")
        if password1 != password2:
            messages.warning(
                request, "Two Password Fields Is Not Matching")
            return redirect("Signup")
        user = User(username=username, email=email)
        user.set_password(password1)
        user.save()
        login(request, user)
        return redirect("Home")
    return render(request, 'signup.html')
