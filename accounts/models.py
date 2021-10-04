from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


INDUSTRY = [
    ('AGRICULTURE', 'Agriculture'),
    ('APPAREL', 'Apparel'),
    ('AUTOMOBILES & MOTORCYCLES', 'Automobiles & Motorcycles'),
    ('BEAUTY & PERSONAL CARE', 'Beauty & Personal Care'),
    ('CHEMICALS', 'Chemicals'),
    ('COMPUTER HARDWARE & SOFTWARE', 'Computer Hardware & Software'),
    ('CONSTRUCTION & REAL ESTATE', 'Construction & Real Estate'),
    ('CONSUMER ELECTRONICS', 'Consumer Electronics'),
    ('ELECTRICAL EQUIPMENT SUPPLIES', 'Electrical Equipment Supplies'),
    ('ENERGY', 'Energy'),
    ('ENVIRONMENT', 'Environment'),
    ('FASHION ACCESSORIES', 'Fashion Accessories'),
    ('FOOD & BEVERAGE', 'Food & Beverage'),
    ('FURNITURE', 'Furniture'),
    ('GIFTS & CRAFTS', 'Gifts & Crafts'),
    ('HARDWARE', 'Hardware'),
    ('HEALTH & MEDICAL', 'Health & Medical'),
    ('HOME & GARDEN', 'Home & Garden'),
    ('HOME APPLIANCES', 'Home Appliances'),
    ('INDUSTRIAL PARTS & FABRICATION SERVICES', 'Industrial Parts & Fabrication Services'),
    ('LIGHTS & LIGHTING', 'Lights & Lighting'),
    ('LUGGAGE, BAGS & CASES', 'Luggage, Bags & Cases'),
    ('MACHINERY', 'Machinery'),
    ('MEASUREMENT & ANALYSIS INSTRUMENTS', 'Measurement & Analysis'),
    ('MINERALS & METALLURGY', 'Minerals & Metallurgy'),
    ('MULTIPLE PRODUCTS', 'Multiple Products'),
    ('OFFICE & SCHOOL SUPPLIES', 'Office & School Supplies'),
    ('PACKING & PRINTING', 'Packing & Printing'),
    ('RUBBER & PLASTICS', 'rubber & Plastics'),
    ('SECURITY & PROTECTION', 'Security & Protection'),
    ('SERVICE EQUIPMENT', 'Service Equipment'),
    ('SHOES & FOOTWEAR ACCESSORIES', 'Shoes & Footwear Accessories'),
    ('SPORTS & ENTERTAINMENT', 'Sports & Entertainment'),
    ('TELECOMMUNICATION', 'Telecommunication'),
    ('TEXTILE & LEATHER PRODUCT', 'Textile & Leather Product'),
    ('TIMEPIECES, JEWELRY , EYEWEAR', 'Timepieces, Jewelry , Eyewear'),
    ('TOOLS', 'Tools'),
    ('TOYS & HOBBIES', 'Toys & Hobbies'),
    ('TRANSPORTATION', 'Transportation'),
]

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]

EMPLOYEE_CHOICES = [
    ("Fewer than 5", "Fewer than 5"),
    ("5 - 10", "5 - 10"),
    ("11 - 50", "11 - 50"),
    ("51 - 100", "51 - 100"),
    ("101 - 200", "101 - 200"),
    ("201 - 300", "201 - 300"),
    ("301 - 400", "301 - 400"),
    ("401 - 500", "401 - 500"),
    ("over 501", "over 501"),
]

TYPE_CHOICES = [
    ("buyer", "Buyer"),
    ("seller", "Seller"),
    ("retailer", "Retailer"),
    ("agent", "Agent"),
]

STATUS = (
    (0, "Verified"),
    (1, "Unverified"),
    (2, "Hold"),
)

BUSSINESS = [
    ("manufacturer", "Manufacturer"),
    ("company", "Trading Company"),
    ("buying Office", "Buying Office"),
    ("agent", "Agent"),
    ("distributor/Wholesaler", "Distributor/Wholesaler"),
    ("government", "Government ministry/Bureau/Commission"),
    ("association", "Association"),
    ("business",
     "Business Service (Transportation, finance, travel, Ads, etc)"),
    ("other", "Other"),
]


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
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    mobile = models.CharField(max_length=120, default='123456789')
    img = models.ImageField(upload_to='pics', default='profile1.png', verbose_name="Profile Image")
    bio = RichTextField(blank=True, null=True)
    aboutus = RichTextField(blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True)
    organization = models.CharField(max_length=230, null=True, blank=True)
    type = models.CharField(max_length=50, choices=BUSSINESS, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    img1 = models.ImageField(upload_to='pics', verbose_name="Profile Image", default='static/vivah/img/profile.jpg')
    img2 = models.ImageField(upload_to='pics', verbose_name="Profile Image", default='static/vivah/img/profile.jpg')
    img3 = models.ImageField(upload_to='pics', verbose_name="Profile Image", default='static/vivah/img/profile.jpg')
    img4 = models.ImageField(upload_to='pics', verbose_name="Profile Image", default='static/vivah/img/profile.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'







