from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from accounts.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab

DOY = ('1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971',
       '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979',
       '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015', '2016', '2017', '2018',)


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
    birthday = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=DOY))

    class Meta:
        model = Profile
        fields = ['img', 'gender', 'martialstatus', 'mobile', 'religion', 'caste', 'birthday',
                  'state', 'searchfor', 'videofile', 'birthplace', 'birthtimehh', 'birthtimemm', 'ampm',
                  'birthstate', 'birthcountry', 'languages', 'horo', 'manglik', 'diet', 'smoke', 'age',
                  'city', 'education',
                  ]

        labels = {
            'smoke': _('Smoking'),
            'diet': _('Diet'),
            'horo': _('Horoscope match is necessary?'),
            'manglik': _('Are you manglik ?'),
            'birthtimehh': _('Hour'),
            'birthtimemm': _('Minute'),
            'birthplace': _('Birth Place'),
            'birthstate': _('Birth State'),
            'birthcountry': _('Birth Country'),
            'ampm': _('AM/PM'),
            'img': _('Profile Image'),
            'gender': _('Sex'),
            'martialstatus': _('Martial Status'),
            'searchfor': _('Parnter Search Perference'),
            'videofile': _('IntroductiionVideo'),
            'caste': _('Sub Caste'),
            'organization': _('EXPECTATIONS'),
            "state": _('Current State'),
            "city": _('Current City'),
            "languages": _('Mother Tongue'),
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
            )
        )
    )

    class Meta:
        model = Profile

        labels = {
            'img': _('Profile Image'),
            'img1': _('Upload Kundali'),
            'img2': _('Family Photo'),
            'img3': _('Profile Image'),
            'img4': _('Profile Image'),
            'zip': _('Pincode'),
            'number': _('Office Contact Numbers'),
            'gender': _('Sex'),
            'martialstatus': _('Martial Status'),
            'searchfor': _('Partner Search Preference'),
            'videofile': _('Introduction Video for yourself'),
            'caste': _('Sub Caste (please specify if any)'),
            'aboutus': _('About Me'),
            'website': _('Website / Facebook Link ')
        }

        fields = ['img', 'videofile', 'img2', 'img3', 'img1', 'img4',
                  'address', 'city', 'zip', 'state', 'number',
                  'mobile', 'website', 'aboutus',
                  ]


class UserUpdForm(forms.ModelForm):
    email = forms.EmailField(disabled=True)
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Preferences
        labels = {
            'profilefo': _('Match for'),
            'organization': _('My ideal partner would be like'),
            'pagemin': _('Minimum Age'),
            'pagemax': _('Maximum Age'),
            'pmartialstatus': _('Martial Status'),
            'pcomplexion': _('Complexion'),
            'preligion': _('Religion'),
            'pcaste': _('Caste'),
            'peducation': _('Education'),
        }
        fields = ['profilefo', 'organization', 'pagemin', 'pagemax', 'pmartialstatus', 'pcomplexion',
                  'preligion', 'pcaste', 'peducation',
                  ]


class FamilyValuesForm(forms.ModelForm):
    class Meta:
        model = FamilyValues
        labels = {
            'height': _('My Height'),
            'aboutfamily': _('About My Family'),
            'father': _('Fathers Occupation'),
            'mother': _('Mothers Occupation'),
            'familystatus': _('Family Status'),
            'familytype': _('Family Type'),
            'familyvalues': _('Family Values'),
            'employed': _('Employed'),
            'designation': _('Designation/Occupation'),
            'annualincome': _('My Annual Income (in lakhs) Rs.'),
            'awards': _('Awards And Certifications [My AchievementsIn Life]'),
        }
        fields = ['height', 'familystatus', 'father', 'mother', 'brother', 'sister', 'familyvalues', 'familytype',
                  'employed',
                  'designation', 'annualincome', 'aboutfamily', 'awards',
                  ]


class ProdCommentForm(forms.ModelForm):
    class Meta:
        model = ProdComment
        fields = ('name', 'email', 'mobile', 'body')





