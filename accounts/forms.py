from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from accounts.models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab


def validate_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError(f"{value} is taken.", params={'value': value})


# Sign Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required', validators=[validate_email])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Profile Form
class ProfileForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    email = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class ProfileUpdateForm(forms.ModelForm):
    birthday = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)

    class Meta:
        model = Profile
        fields = ['img', 'gender', 'martialstatus', 'mobile', 'religion', 'caste', 'birthday',
                  'state', 'searchfor', 'videofile',
                  ]

        labels = {
            'img': _('Profile Image'),
            'gender': _('Sex'),
            'martialstatus': _('Martial Status'),
            'searchfor': _('Parnter Search Perference'),
            'videofile': _('IntroductiionVideo'),
            'caste': _('Sub Caste (please specify if any)'),
            'organization': _('EXPECTATIONS'),
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(disabled=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        TabHolder(
            Tab(
                'Image / Videos',
                'img',
                'videofile',
                'img1',
                'img2',
                'img3',
                'img4',
            ),
            Tab(
                'Address',
                'address',
                'city',
                'state',
                'zip'
            ),
            Tab(
                'Contact',
                'mobile',
                'number',
                'website',
                'aboutus',
                'organization',
            )
        )
    )

    class Meta:
        model = Profile

        labels = {
            'img': _('Profile Image'),
            'img1': _('Upload Kundali'),
            'img2': _('Profile Image-2'),
            'img3': _('Profile Image-3'),
            'img4': _('Profile Image-4'),
            'zip': _('Pincode'),
            'number': _('Office Contact Numbers'),
            'gender': _('Sex'),
            'martialstatus': _('Martial Status'),
            'searchfor': _('Partner Search Preference'),
            'videofile': _('Introduction Video for yourself'),
            'caste': _('Sub Caste (please specify if any)'),
            'aboutus': _('About Me'),
            'organization': _('What I Am Looking For?'),

        }

        fields = ['img', 'videofile', 'img1', 'img2', 'img3', 'img4',
                  'address', 'city', 'zip', 'state', 'number',
                  'mobile', 'organization', 'website', 'aboutus',
                  ]


class UserUpdForm(forms.ModelForm):
    email = forms.EmailField(disabled=True)
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ['username', 'email']
