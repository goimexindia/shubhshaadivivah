from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.views import View
from django.contrib import messages
from accounts.models import Profile, Notification
from shubhshaadivivah import settings
from socials.forms import MessageForm, ThreadForm
from socials.models import ThreadModel, MessageModel
from vivah.models import Contactme
from django.contrib.auth.models import User
from django.template.loader import render_to_string


def event(request):
    email = request.POST['email']
    msg_plain = render_to_string('email.txt', {'some_params': 'testing'})
    msg_html = render_to_string('vivah/event.html', {'some_params': 'testing'})
    to_list = [email, settings.EMAIL_HOST_USER]
    from_email = settings.EMAIL_HOST_USER
    send_mail(
        'email title',
        msg_plain,
        from_email,
        to_list,
        html_message=msg_html,
    )
    return render(request, 'vivah/event.html')


def home(request):
    return render(request, 'vivah/index.html',
                  {'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
                   })

@login_required
def productcontact(request):
    return render(request, 'vivah/productcontact.html',
                  {'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
                   })


@login_required(login_url='login')
def homeregister(request):
    return render(request, 'vivah/index.html', {})


@login_required
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


class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))

        context = {
            'threads': threads
        }

        return render(request, 'social/inbox.html', context)


class CreateThread(View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()

        context = {
            'form': form
        }

        return render(request, 'social/create_thread.html', context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)
        username = request.POST.get('username')

        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('thread', pk=thread.pk)
            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('thread', pk=thread.pk)

            if form.is_valid():
                thread = ThreadModel(
                    user=request.user,
                    receiver=receiver
                )
                thread.save()

                return redirect('thread', pk=thread.pk)
        except:
            messages.error(request, 'Invalid username')
            return redirect('create-thread')


class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        context = {
            'thread': thread,
            'form': form,
            'message_list': message_list
        }

        return render(request, 'social/thread.html', context)


class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        form = MessageForm(request.POST, request.FILES)
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        if form.is_valid():
            message = form.save(commit=False)
            body = message.body
            message.thread = thread
            message.sender_user = request.user
            message.receiver_user = receiver
            message.save()

        notification = Notification.objects.create(
            notification_type=4,
            sender=request.user,
            recipient=receiver,
            message=body,
            thread=pk,
        )
        return redirect('thread', pk=pk)


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
        message = request.POST['message'] + " - " + request.POST['email']
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
        #send_mail(subject, message, from_email, to_list, fail_silently=True)

        html_content = render_to_string('vivah/event.html', {'varname': 'value'})  # render with dynamic value
        text_content = strip_tags(html_content)  # Strip the html tag. So people can see the pure text at least.
        # create the email, and attach the HTML version as well.
        to_list = [email, settings.EMAIL_HOST_USER]
        from_email = settings.EMAIL_HOST_USER
        msg = EmailMultiAlternatives('EVENT-JAN-2022 SHUBHSHAADIVIVAH', text_content, from_email, to_list)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
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


def EcomerceView1(request):
    all_products = Profile.objects.filter(caste=request.user.profile.caste).order_by("-id")
    paginator = Paginator(all_products, 8)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    product = product_list
    return render(request, 'vivah/product.html', {'product_list': product})


def EcomerceView2(request):
    all_products = Profile.objects.filter(city=request.user.profile.city).order_by("-id")
    paginator = Paginator(all_products, 8)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    product = product_list
    return render(request, 'vivah/product.html', {'product_list': product})


def EcomerceView3(request):
    all_products = Profile.objects.filter(state=request.user.profile.state).order_by("-id")
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
                                         Q(id__exact=search_product) |
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
    return render(request, 'vivah/product.html', {'product_list': product_list, 'page': page})
