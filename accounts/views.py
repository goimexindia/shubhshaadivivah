from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from shubhshaadivivah import settings
from vivah.models import Contactme
from django.contrib.auth.models import User, auth


def register(request):
    return render(request, 'register.html', {'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "Logged IN successfully!")
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('accounts/login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, "Logged OUT successfully!")
    return redirect('/')
