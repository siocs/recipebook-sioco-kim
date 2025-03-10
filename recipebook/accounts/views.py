from django.shortcuts import render


def custom_login(request):
    return render(request, 'registration/login.html')


def custom_logout(request):
    return render(request, 'registration/logout.html')
