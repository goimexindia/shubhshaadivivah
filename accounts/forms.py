from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from accounts.models import Profile


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
        fields = ['img','gender', 'martialstatus', 'mobile', 'religion', 'caste', 'birthday',
                  'state', 'searchfor',
                  ]

        labels = {
            'img': _('Profile Image'),
            'gender': _('Sex'),
            'martialstatus': _('Martial Status'),
            'searchfor': _('Parnter Search Perference'),
            'caste': _('Sub Caste (please specify if any)')
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(disabled=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
