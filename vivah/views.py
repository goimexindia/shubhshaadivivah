from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import TemplateView, ListView

from accounts.forms import UserUpdateForm, ProfileUpdateForm
from accounts.models import Profile
from shubhshaadivivah import settings
from vivah.models import Contactme


def home(request):
    return render(request, 'vivah/index.html',
                  {'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
                   })


def productcontact(request):
    return render(request, 'vivah/productcontact.html',
                  {'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
                   })


@login_required(login_url='login')
def homeregister(request):
    return render(request, 'vivah/index.html', {})


def product(request):
    return render(request, 'vivah/product.html', {})


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
    return render(request, 'vivah/register.html', {})


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


@login_required
def EcomerceView(request):
    all_products = Profile.objects.order_by("-id")
    paginator = Paginator(all_products, 8)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    product = product_list
    return render(request, 'vivah/product.html', {'product_list': product})


def catsearch(request):
    search_product = request.GET.get('search')
    if search_product:
        product = Profile.objects.filter(Q(religion__icontains=search_product) |
                                        Q(caste__icontains=search_product) |
                                        Q(state__icontains=search_product) |
                                        Q(city__icontains=search_product))
    else:
        product = Profile.objects.order_by("-id")
    paginator = Paginator(product, 58)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        product_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        product_list = paginator.page(paginator.num_pages)
    return render(request,  'vivah/product.html', {'product_list': product_list, 'page': page})


