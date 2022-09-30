import django.http
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def reverse(request):
    user_text = request.GET("username")
    rever = user_text[::-1]
    return render(request, 'reverse.html', {'word': rever})
