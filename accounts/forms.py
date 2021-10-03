from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


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
