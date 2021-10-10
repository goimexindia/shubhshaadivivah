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

STATUS = (
    (0, "Verified"),
    (1, "Unverified"),
    (2, "Hold"),
)

MARTIAL_STATUS = [
    ('single', "Single"),
    ('married', "Married"),
    ('divorced', "Divorced"),
    ('widowed', "Widowed")
]
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=60)


class Whatyouwant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=60)
    product_want = models.EmailField(max_length=260)
    full_name = models.EmailField(max_length=70)
    company_name = models.EmailField(max_length=120)
    phone_number = models.EmailField(max_length=30)
    type = models.EmailField(max_length=60)


class ColdCoffe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    birthday = models.DateField(null=True, blank=True)
   #birthday = models.DateField(null=True, blank=True, validators=[MinAgeValidator(18)])
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
    organization =  RichTextField(blank=True, null=True)
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
