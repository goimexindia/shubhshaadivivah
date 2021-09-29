from django.shortcuts import render
from django.core.mail import send_mail
from shubhshaadivivah import settings
from vivah.models import Contactme


def home(request):
    return render(request, 'vivah/index.html', {'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY})


def homeregister(request):
    return render(request, 'vivah/index.html', {})


def ellite(request):
    return render(request, 'vivah/ellite.html', {})


def about(request):
    return render(request, 'vivah/about.html', {})

def secure(request):
    return render(request, 'vivah/staysecure.html', {})


def disclaimer(request):
    return render(request, 'vivah/disclaimer.html', {})


def privacy(request):
    return render(request, 'vivah/privacy.html', {})


def terms(request):
    return render(request, 'vivah/terms.html', {})


def faq(request):
    return render(request, 'vivah/faq.html', {})


def pricing(request):
    return render(request, 'vivah/index.html', {})


def services(request):
    return render(request, 'vivah/services.html', {})


def membership(request):
    return render(request, 'vivah/membership.html', {})


def register(request):
    return render(request, 'vivah/all-in-one.html', {})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        mobile = request.POST['phone']
        message = request.POST['message']
        subject = "Thank you for contacting ShubhShaadiVivah.com."
        message = "Dear " + name + ",\n\n" \
                  + "We will get in touch with you soon." + "\n\n\n" \
                  + "Your message details : -" + "\n" \
                  + "Message From-" + name + "\n" \
                  + "Email:-" + email + "\n\n" \
                  + "Mobile:-" + phone + "\n\n" \
                  + "Subject-" + subject + "\n\n" \
                  + "Details-" + message + "\n\n\n" \
                  + "Warm Regards \n\n From: ShubhShaadiVivah Support Team"
        from_email = settings.EMAIL_HOST_USER
        to_list = [email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        contactme = Contactme(name=name, email=email, mobile=mobile, subject=subject, message=message)
        contactme.save()

        return render(request, 'vivah/contact.html', {'name': name, 'email': email})
    else:
        return render(request, 'vivah/contact.html', {})
