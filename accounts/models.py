from importlib._common import _

from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from datetime import date
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from ckeditor.fields import RichTextField

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]

EMPLOYED = [
    ("Self Employed", "Self Employed"),
    ("Business", "Business"),
    ("Government", "Government"),
    ("PSU", "PSU"),
    ("MNC", "MNC"),
    ("Defence", "Defence"),
    ("Private", "Private"),
    ("Not Working", "Not Working"),
]

FAMILYTYPE = [
    ("Nuclear", "Nuclear"),
    ("Joint", "Joint")
]

FAMILYVALUES = [
    ("Orthodox", "Orthodox"),
    ("Tradational", "Tradational"),
    ("Moderate", "Moderate"),
    ("Liberal", "Liberal"),
]

FAMILYSTATUS = [
    ("Middle Class", "Middle Class"),
    ("Upper Middle Class", "Upper Middle Class"),
    ("Rich", "Rich"),
    ("Elite", "Elite"),
]

HEIGHT = [
    ("4-6", "4ft 6in / 137 cms"),
    ("4-7", "4ft 7in / 139 cms"),
    ("4-8", "4ft 8in / 142 cms"),
    ("4-9", "4ft 9in / 144 cms"),
    ("4-10", "4ft 10in / 147 cms"),
    ("4-11", "4ft 11in / 149 cms"),
    ("5", "5ft / 152 cms"),
    ("5-1", "5ft 1in / 154 cms"),
    ("5-2", "5ft 2in / 157 cms"),
    ("5-3", "5ft 3in / 160 cms"),
    ("5-4", "5ft 4in / 162 cms"),
    ("5-5", "5ft 5in / 165 cms"),
    ("5-6", "5ft 6in / 167 cms"),
    ("5-7", "5ft 7in / 170 cms"),
    ("5-8", "5ft 8in / 172 cms"),
    ("5-9", "5ft 9in / 175 cms"),
    ("5-10", "5ft 10in / 177cms"),
    ("5-11", "5ft 11in / 180 cms"),
    ("6", "6ft / 182 cms"),
    ("6-1", "6ft 1 in / 185 cms"),
    ("6-2", "6ft 2in / 187 cms"),
    ("6-3", "6ft 3in / 190 cms"),
    ("6-4", "6ft 4in / 193 cms"),
    ("6-5", "6ft 5in / 195 cms"),
    ("6-6", "6ft 6in / 198 cms"),
]

MOTHERTONGUE = [
    ("Bengali", "Bengali"),
    ("Gujarati", "Gujarati"),
    ("Hindi", "Hindi"),
    ("Kannada", "Kannada"),
    ("Malayalam", "Malayalam"),
    ("Marathi", "Marathi"),
    ("Marwari", "Marwari"),
    ("Oriya", "Oriya"),
    ("Punjabi", "Punjabi"),
    ("Sindhi", "Sindhi"),
    ("Tamil", "Tamil"),
    ("Telugu", "Telugu"),
    ("Urdu", "Urdu")
]

PROFILEFOR = [
    ("Myself", "Myself"),
    ("Son", "Son"),
    ("Daughter", "Daughter"),
    ("Brother", "Brother"),
    ("Sister", "Sister"),
    ("Relative", "Relative"),
    ("Friend", "Friend"),
]

COMPLEXION = (
    ("Fair", "Fair"),
    ("Very Fair", "Very Fair"),
    ("Medium", "Medium"),
    ("Brown", "Brown"),
    ("Dark", "Dark"),
    ("Any Complexion", "Any Complexion")

)
STATUS = (
    (0, "Verified"),
    (1, "Unverified"),
    (2, "Hold"),
)
BIRTHTIME = (
    ("01", "01"),
    ("02", "02"),
    ("03", "03"),
    ("04", "04"),
    ("05", "05"),
    ("06", "06"),
    ("07", "07"),
    ("08", "08"),
    ("09", "09"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
)

AMPM = (
    ("AM", "AM"),
    ("PM", "PM"),
)

AGE = (
    ("01", "01"),
    ("02", "02"),
    ("03", "03"),
    ("04", "04"),
    ("05", "05"),
    ("06", "06"),
    ("07", "07"),
    ("08", "08"),
    ("09", "09"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ("13", "13"),
    ("14", "14"),
    ("15", "15"),
    ("16", "16"),
    ("17", "17"),
    ("18", "18"),
    ("19", "19"),
    ("20", "20"),
    ("21", "21"),
    ("22", "22"),
    ("23", "23"),
    ("24", "24"),
    ("25", "25"),
    ("26", "26"),
    ("27", "27"),
    ("28", "28"),
    ("29", "29"),
    ("30", "30"),
    ("31", "31"),
    ("32", "32"),
    ("33", "33"),
    ("34", "34"),
    ("35", "35"),
    ("36", "36"),
    ("37", "37"),
    ("38", "38"),
    ("39", "39"),
    ("40", "40"),
    ("41", "41"),
    ("42", "42"),
    ("43", "43"),
    ("44", "44"),
    ("45", "45"),
    ("46", "46"),
    ("47", "47"),
    ("48", "48"),
    ("49", "49"),
    ("50", "50"),
    ("51", "51"),
    ("52", "52"),
    ("53", "53"),
    ("54", "54"),
    ("55", "55"),
    ("56", "56"),
    ("57", "57"),
    ("58", "58"),
    ("59", "59"),
    ("60", "60"),
)

MARTIAL_STATUS = [
    ('single', "Single"),
    ('married', "Married"),
    ('divorced', "Divorced"),
    ('waiting for divorced', "Waiting For Divorced"),
    ('widowed', "Widowed"),
    ('any status', "Any Status"),
]

EDUCATION = [
    ("99", "Bachelors - Engineering / Computers / Others"),
    ("100", "Masters - Engineering / Computers / Others"),
    ("101", "Bachelors - Arts / Science / Commerce / Others"),
    ("102", "Masters - Arts / Science / Commerce / Others"),
    ("103", "Bachelors - Management / Others "),
    ("104", "Masters - Management / Others"),
    ("105", "Bachelors - Medicine - General / Dental / Surgeon / Others"),
    ("106", "Masters - Medicine - General / Dental / Surgeon / Others"),
    ("107", "Bachelors - Legal / Others"),
    ("108", "Masters - Legal / Others"),
    ("109", "Finance - ICWAI / CA / CS / CFA / Others"),
    ("110", "Service - IAS / IPS / IRS / IES / IFS / Others"),
    ("111", "PhD"),
    ("112", "Diploma / Others"),
    ("114", "Higher Secondary / Secondary"),
    ("215", "Others"), ]

STATE = (("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"),
         ("Chandigarh (UT)", "Chandigarh (UT)"),
         ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"),
         ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"),
         ("Jammu and Kashmir ", "Jammu and Kashmir "), ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"),
         ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"),
         ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"), ("Nagaland", "Nagaland"),
         ("Odisha", "Odisha"), ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"), ("Sikkim", "Sikkim"),
         ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"),
         ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"),
         ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"),
         ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"),
         ("Lakshadweep", "Lakshadweep"), ("Pondicherry(UT)", "Pondicherry(UT)"),
         ("National Capital Territory of Delhi", "National Capital Territory of Delhi"),
         ("Puducherry", "Puducherry"))
RELIGION = [
    ("Religion", "Tamil"),
    ("Hindu", "Hindu"),
    ("Muslim - Shia", "Muslim - Shia"),
    ("Muslim - Sunni", "Muslim - Sunni"),
    ("Muslim - Others", "Muslim - Others"),
    ("Christian", "Christian"),
    ("Sikh", "Sikh"),
    ("Jain - Digambar", "Jain - Digambar"),
    ("Jain - Shwetambar", "Jain - Shwetambar"),
    ("Jain - Others", "Jain - Others"),
    ("Parsi", "Parsi"),
    ("Buddhist", "Buddhist"),
    ("Inter-Religion", "Inter - Religion"),
    ("Caste No Bar", "Caste No Bar")
]


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


@deconstructible
class MinAgeValidator(BaseValidator):
    message = _("Age must be at least %(limit_value)d.")
    code = 'min_age'

    def compare(self, a, b):
        return calculate_age(a) < b


class Subscriber(models.Model):
    email = models.EmailField(max_length=60)


class Whatyouwant(models.Model):
    email = models.EmailField(max_length=60)
    product_want = models.EmailField(max_length=260)
    full_name = models.EmailField(max_length=70)
    company_name = models.EmailField(max_length=120)
    phone_number = models.EmailField(max_length=30)
    type = models.EmailField(max_length=60)


class ColdCoffe(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, default='123456789')
    address = models.CharField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Customer'

    def get_absolute_url(self):
        return reverse('customer-detail', args=[str(self.id)])

    class Meta:
        ordering = ['full_name']


class Preferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilefo = models.CharField(max_length=20, choices=PROFILEFOR, null=True, blank=True)
    organization = RichTextField(blank=True, null=True)
    pagemin = models.CharField(max_length=20, choices=AGE, null=True, blank=True)
    pagemax = models.CharField(max_length=20, choices=AGE, null=True, blank=True)
    pmartialstatus = models.CharField(max_length=20, choices=MARTIAL_STATUS, null=True, blank=True)
    pcomplexion = models.CharField(max_length=20, choices=COMPLEXION, null=True, blank=True)
    preligion = models.CharField(max_length=50, choices=RELIGION, null=True, blank=True)
    peducation = models.CharField(max_length=50, choices=EDUCATION, null=True, blank=True)
    pcaste = models.CharField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.user.username} Preferences'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilefo = models.CharField(max_length=20, choices=PROFILEFOR, default="Myself")
    email_confirmed = models.BooleanField(default=False)
    birthday = models.DateField(null=True, blank=True)
    birthtimehh = models.CharField(max_length=10, choices=BIRTHTIME, null=True, blank=True)
    birthtimemm = models.CharField(max_length=10, choices=AGE, null=True, blank=True)
    birthplace = models.CharField(max_length=100, default="PUNE")
    birthstate = models.CharField(max_length=100, choices=STATE, default="MAHARASHTRA")
    birthcountry = models.CharField(max_length=100, default="INDIA")
    ampm = models.CharField(max_length=4, choices=AMPM, default="AM")
    languages = models.CharField(max_length=100, choices=MOTHERTONGUE, default="Hindi")
    # birthday = models.DateField(null=True, blank=True, validators=[MinAgeValidator(18)])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Male")
    mobile = models.CharField(max_length=120, default='123456789')
    religion = models.CharField(max_length=50, choices=RELIGION, default='HINDU')
    caste = models.CharField(max_length=120, default='HINDU')
    searchfor = models.CharField(max_length=50, choices=RELIGION, default='HINDU')
    martialstatus = models.CharField(max_length=20, choices=MARTIAL_STATUS, default='Single')
    img = models.ImageField(upload_to='pics', default='profile.jpg', verbose_name='static/pic/img/profile.jpg')
    bio = models.CharField(max_length=255, null=True, blank=True)
    aboutus = RichTextField(blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(choices=STATE, max_length=150, null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="", default='videos/Krishna.mp4')
    img1 = models.ImageField(upload_to='pics', verbose_name="Profile Image", default='static/vivah/img/profile.jpg')
    img2 = models.ImageField(upload_to='pics', verbose_name="Profile Image", default='static/vivah/img/profile.jpg')
    img3 = models.ImageField(upload_to='pics', verbose_name="Profile Image", default='static/vivah/img/profile.jpg')
    img4 = models.ImageField(upload_to='pics', verbose_name="Profile Image", default='static/vivah/img/profile.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'


class FamilyValues(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.CharField(max_length=100, choices=HEIGHT, null=True, blank=True)
    familystatus = models.CharField(max_length=100, choices=FAMILYSTATUS, null=True, blank=True)
    familytype = models.CharField(max_length=100, choices=FAMILYTYPE, null=True, blank=True)
    familyvalues = models.CharField(max_length=100, choices=FAMILYVALUES, null=True, blank=True)
    disability = models.CharField(max_length=100, null=True, blank=True)
    employed = models.CharField(max_length=100, choices=EMPLOYED, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    annualincome= models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} FamilyValues'