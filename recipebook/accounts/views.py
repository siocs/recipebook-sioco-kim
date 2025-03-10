from django.shortcuts import render


def custom_login(request):
    return render(request, 'registration/login.html')
