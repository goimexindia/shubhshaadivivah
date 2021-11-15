from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator
from django.db.models import OuterRef, Exists
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django import forms
from crispy_forms.helper import FormHelper
from rest_framework.utils import json

from accounts.filters import OrderFilter
from accounts.models import Profile, ViewComment
from accounts.token import account_activation_token
from shubhshaadivivah import settings
from vivah.models import Contactme
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from accounts.forms import *
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives


def register(request):
    return render(request, 'vivah/register.html', {'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY})


def insert(request):
    email = request.POST['emailId']
    member = Event(email=request.POST['emailId'], )
    member.save()

    html_content = render_to_string('vivah/event.html', {'varname': 'value'})  # render with dynamic value
    text_content = strip_tags(html_content)  # Strip the html tag. So people can see the pure text at least.
    # create the email, and attach the HTML version as well.
    to_list = [email, settings.EMAIL_HOST_USER]
    from_email = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives('EVENT-JAN-2022 SHUBSHAADIVIVAH', text_content, from_email, to_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return redirect('/')


def postdetails(request):
    posts = get_object_or_404(Profile, pk=request.user.profile.id)
    print(request.user.profile.id)
    post_likes = posts.likes.all()
    return render(request, 'accounts/post_details02.html', {'post_likes': post_likes})


def eventinfo(request):
    return render(request, 'vivah/eventinfo.html', {'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY})


def success(request):
    return render(request, 'vivah/success.html', {'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY})


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
    template_name = 'vivah/profile.html'
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


def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'religion': user.profile.religion,
                                                          'mobile': user.profile.mobile,
                                                          'gender': user.profile.gender,
                                                          'birthday': user.profile.birthday,
                                                          'state': user.profile.state,
                                                          'searchfor': user.profile.searchfor,
                                                          'caste': user.profile.caste,
                                                          'martialstatus': user.profile.martialstatus,
                                                          })


def handlesignup(request):
    if request.method == 'POST':
        # get the post parameters
        uname = request.POST["uname"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        profilefor = request.POST["ProfileFor"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        martialstatus = request.POST["MartialStatus"]
        age1 = request.POST["age1"]
        state = request.POST["State"]
        city = request.POST["city"]
        zip = request.POST["zip"]
        dob = request.POST["dob"]
        gender = request.POST["gender"]
        religion = request.POST["Religion"]
        caste = request.POST["caste"]
        mobile = request.POST["mobile"]
        gender = request.POST["gender"]
        birthday = request.POST["dob"]
        searchfor = request.POST["SearchFor"]
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
            if email_exists:
                messages.error(
                    request, " EMAIL already taken..., Please try again")
                return redirect("home")
        # create the user
        user = User.objects.create_user(uname, email, password1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        user.refresh_from_db()
        userid = user.id
        user.profile.religion = religion
        user.profile.mobile = mobile
        user.profile.birthday = dob
        user.profile.gender = gender
        user.profile.birthday = birthday
        user.profile.state = state
        user.profile.city = city
        user.profile.age = age1
        user.profile.zip = zip
        user.profile.gender = gender
        user.profile.caste = caste
        user.profile.searchfor = searchfor
        user.profile.martialstatus = martialstatus
        user.profile.profilefo = profilefor
        update_user_data(user)
        user.save()

        raw_password = password1

        # login user after signing up
        user = authenticate(username=user.username, password=raw_password)

        AuthenticationForm(request=request, data=request.POST)

        messages.success(
            request, " Your account has been successfully created. UserID:" + str(userid))
        return redirect("login")
    else:
        return HttpResponse('404 - NOT FOUND ')


def usercommettype(request, pk=id):
    if request.method == 'POST':
        status = request.POST["status"]
        obj = ProdComment.objects.get(pk=pk)
        obj.status = status
        obj.save()
    return redirect('userprofile')


def handlesignup1(request):
    if request.method == 'POST':
        # get the post parameters
        uname = request.POST["uname"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        profilefor = request.POST["ProfileFor"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        martialstatus = request.POST["MartialStatus"]
        age1 = request.POST["age1"]
        state = request.POST["State"]
        city = request.POST["city"]
        zip = request.POST["zip"]
        dob = request.POST["dob"]
        religion = request.POST["Religion"]
        caste = request.POST["caste"]
        mobile = request.POST["mobile"]
        gender = request.POST["gender"]
        birthday = request.POST["dob"]
        searchfor = request.POST["SearchFor"]
        session = request.POST["PreferedSession"]
        eventday = request.POST["PreferedDate"]
        # check for errors in input
        if request.method == 'POST':
            try:
                user_exists = User.objects.get(username=request.POST['uname'])
                messages.error(
                    request, " Username already taken, Try something else!!!")
                return redirect("eventsignup")
            except User.DoesNotExist:
                if len(uname) <= 15:
                    pass
                else:
                    messages.error(
                        request, " Username must be max 15 characters, Please try again")
                    return redirect("eventsignup")
            if not uname.isalnum():
                messages.error(
                    request, " Username should only contain letters and numbers, Please try again")
                return redirect("eventsignup")
            if password1 != password2:
                messages.error(
                    request, " Password do not match, Please try again")
                return redirect("eventsignup")

            if not uname.isalnum():
                messages.error(
                    request, " Username should only contain letters and numbers, Please try again")
                return redirect("eventsignup")
            if password1 != password2:
                messages.error(
                    request, " Password do not match, Please try again")
                return redirect("eventsignup")
            email_exists = User.objects.filter(email=request.POST['email'])
            if email_exists:
                messages.error(
                    request, " EMAIL already taken..., Please try again")
                return redirect("eventsignup")
        # create the user
        user = User.objects.create_user(uname, email, password1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        user.refresh_from_db()
        userid = user.id
        user.profile.religion = religion
        user.profile.mobile = mobile
        user.profile.birthday = dob
        user.profile.gender = gender
        user.profile.birthday = birthday
        user.profile.state = state
        user.profile.city = city
        user.profile.age = age1
        user.profile.zip = zip
        user.profile.caste = caste
        user.profile.searchfor = searchfor
        user.profile.martialstatus = martialstatus
        user.profile.profilefo = profilefor
        user.profile.eventday = eventday
        user.profile.session = session

        update_user_data(user)
        user.save()

        raw_password = password1

        # login user after signing up
        user = authenticate(username=user.username, password=raw_password)

        AuthenticationForm(request=request, data=request.POST)

        messages.success(
            request, " Your account has been successfully created. UserID:" + str(userid))
        return redirect("success")
    else:
        return HttpResponse('404 - NOT FOUND ')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile data has been updatedd!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'pinterestsent': 0,
        'pinterestreceived': 0,
        'pvisitor': 0,
        'pinterestaccepted': 0,
        'pintreject': 0,
        'pshortlist': 0,
        'pcontactview': 0,
        'membership': 'FREE',
    }
    return render(request, 'vivah/profile.html', context)


@login_required
def profile1(request):
    if request.method == 'POST':
        p_form = UserForm(request.POST,
                          request.FILES,
                          instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your profile data has been updatedd!')
            return redirect('profile1')
        else:
            messages.error(request, f'Your profile data has errors!!!!!!')
            return redirect('profile1')
    else:
        p_form = UserForm(instance=request.user.profile)
    context = {
        'p_form': p_form,
    }
    return render(request, 'vivah/profile1.html', context)


@login_required
def profilepref(request):
    print(request.method)
    if request.method == 'POST':
        print("2")
        p_form = PartnerForm(request.POST,
                             request.FILES,
                             instance=request.user.preferences)
        if p_form.is_valid():
            print("4")
            p_form.save()
            messages.success(request, f'Your profile data has been updatedd!')
            return redirect('profilepref')
        else:
            messages.error(request, f'Your profile data has errors!!!!!!')
            return redirect('profilepref')
    else:
        p_form = PartnerForm(instance=request.user.preferences)
    context = {
        'p_form': p_form,
    }
    return render(request, 'vivah/profile2.html', context)


@login_required
def familyvalues(request):
    print(request.method)
    if request.method == 'POST':
        print("2")
        p_form = FamilyValuesForm(request.POST,
                                  request.FILES,
                                  instance=request.user.familyvalues)
        if p_form.is_valid():
            print("4")
            p_form.save()
            messages.success(request, f'Your familyvalues data has been updatedd!')
            return redirect('familyvalues')
        else:
            messages.error(request, f'Your familyvalues data has errors!!!!!!')
            return redirect('familyvalues')
    else:
        p_form = FamilyValuesForm(instance=request.user.familyvalues)
    context = {
        'p_form': p_form,
        'pinterestsent': 0,
        'pinterestreceived': 0,
        'pvisitor': 0,
        'pinterestaccepted': 0,
        'pintreject': 0,
        'pshortlist': 0,
        'pcontactview': 0,
        'membership': 'FREE',

    }
    return render(request, 'vivah/profile5.html', context)


class NoFormTagCrispyFormMixin(object):
    @property
    def helper(self):
        if not hasattr(self, '_helper'):
            self._helper = FormHelper()
            self._helper.form_tag = False
        return self._helper


@login_required
def userprofile(request):
    posts = get_object_or_404(Profile, pk=request.user.profile.id)
    print(request.user.profile.id)
    post_likes = posts.likes.all()
    print(post_likes)
    if request.method == 'POST':
        p_form = UserForm(request.POST,
                          request.FILES,
                          instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your profile data has been updatedd!')
            return redirect('profile1')
        else:
            messages.error(request, f'Your profile data has errors!!!!!!')
            return redirect('profile1')
    else:
        p_form = UserForm(instance=request.user.profile)
    context = {
        'p_form': p_form, 'post_likes': post_likes,
    }
    return render(request, 'vivah/userprofile.html', context)


def shaadiprofile(request, pk):
    customer = Profile.objects.get(id=pk)
    if request.user.is_authenticated:
        customer.view_count += 1
        customer.save()
        contactme = ViewComment(userview=pk, userrequest=request.user.id)
        contactme.save()

    liked = False
    if customer.likes.filter(id=request.user.id).exists():
        liked = False
    else:
        liked = True
    context = {'customers': customer, 'liked': liked}
    return render(request, 'accounts/shaadiprofile.html', context)


def prodcomment(request, pk):
    template_name = 'vivah/prodcomment.html'
    product = Profile.objects.get(id=pk)
    comments = product.prodcomment.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = ProdCommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            receiver = product.user
            body = new_comment.body
            new_comment.userrequest = request.user.id
            # Save the comment to the database
            new_comment.save()
            pk1 = new_comment.id
            notification = Notification.objects.create(
                notification_type=12,
                sender=request.user,
                recipient=receiver,
                message=body,
                thread=pk1,
            )

    else:
        comment_form = ProdCommentForm()

    return render(request, template_name, {'product': product,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def eventsignup(request):
    return render(request, 'accounts/eventsignup.html',
                  {'recaptcha_site_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,
                   })


@login_required
def customer(request):
    orders = Profile.objects.all().order_by('-id')
    myFilter = OrderFilter(request.GET, queryset=orders)
    tableFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    paginator = Paginator(orders, 9)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    orders = product_list

    context = {'orders': orders, 'tableFilter': tableFilter, }
    return render(request, 'accounts/customer.html', context)


def like(request, pk):
    post = get_object_or_404(Profile, id=request.POST.get('post_id'))
    print(request.POST.get('post_id'))
    liked = False
    print(request.user.id)
    print(liked)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
        print(liked)
        print(request.user.id)
    else:
        post.likes.add(request.user)
        liked = True
        print(liked)
    return HttpResponseRedirect(reverse('shaadiprofile', args=[str(pk)]))


class ThreadNotification(View):
    def get(self, request, notification_pk, object_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)
        thread = ThreadModel.objects.get(pk=object_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('thread', pk=object_pk)


class RemoveNotification(View):
    def delete(self, request, notification_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)

        notification.user_has_seen = True
        notification.save()

        return HttpResponse('Success', content_type='text/plain')


class PostNotification(View):
    def get(self, request, notification_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)
        thread = ProdComment.objects.get(pk=notification.thread)

        notification.user_has_seen = True
        notification.save()

        return redirect('post-detail', pk=notification.thread)


class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = ProdComment.objects.get(pk=pk)
        form = CommentForm()

        comments = ProdComment.objects.filter(pk=pk).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'accounts/post_details.html', context)


class FollowNotification(View):
    def get(self, request, notification_pk, profile_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)
        profile = ProdComment.objects.get(pk=profile_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('profile', pk=profile_pk)
