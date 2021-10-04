from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View

from accounts.token import account_activation_token
from shubhshaadivivah import settings
from vivah.models import Contactme
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from accounts.forms import *


def register(request):
    return render(request, 'vivah/register.html', {'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY})


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
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, "Logged OUT successfully!")
    return redirect('/')


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        get_recaptcha = request.POST.get("g-recaptcha-response")
        if form.is_valid():
            email = request.POST['email']
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your ShubhShaadiVivah account.'
            to_email = form.cleaned_data.get('email')
            from_email = settings.EMAIL_HOST_USER
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
            messages.success(request, 'Please Confirm your email to complete registration.')
            return redirect('signup')
            ###return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


class ProfileView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/profile.html'
    success_message = 'PROFILE successfully saved!!!!'


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            # user.profile.email_confirmed = True
            user.save()
            login(request)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('login')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('login')


def handlesignup(request):
    if request.method == 'POST':
        # get the post parameters
        uname = request.POST["uname"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        martialstatus = request.POST["MartialStatus"]
        state = request.POST["State"]
        dob = request.POST["dob"]
        searchfor = request.POST["SearchFor"]
        religion = request.POST["Religion"]
        caste = request.POST["caste"]
        # check for errors in input
        if request.method == 'POST':
            try:
                user_exists = User.objects.get(username=request.POST['uname'])
                messages.error(
                    request, " Username already taken, Try something else!!!")
                return redirect("home")
            except User.DoesNotExist:
                if len(uname) <= 15:
                    pass
                else:
                    messages.error(
                        request, " Username must be max 15 characters, Please try again")
                    return redirect("home")
            if not uname.isalnum():
                messages.error(
                    request, " Username should only contain letters and numbers, Please try again")
                return redirect("home")
            if password1 != password2:
                messages.error(
                    request, " Password do not match, Please try again")
                return redirect("home")

            if not uname.isalnum():
                messages.error(
                    request, " Username should only contain letters and numbers, Please try again")
                return redirect("home")
            if password1 != password2:
                messages.error(
                    request, " Password do not match, Please try again")
                return redirect("home")
            email_exists = User.objects.filter(email=request.POST['email'])
            if email_exists :
                messages.error(
                    request, " EMAIL already taken..., Please try again")
                return redirect("home")
        # create the user
        user = User.objects.create_user(uname, email, password1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(
            request, " Your account has been successfully created")
        return redirect("/")
    else:
        return HttpResponse('404 - NOT FOUND ')
