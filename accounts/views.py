from django.shortcuts import render
from django.core.mail import send_mail
from shubhshaadivivah import settings
from vivah.models import Contactme


def register(request):
    return render(request, 'vivah/register.html', {'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY})