from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def acceder(request):
    return render(request, 'login.html')
