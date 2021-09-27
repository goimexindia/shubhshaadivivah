from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('faq', views.faq, name="faq"),
    path('privacy', views.privacy, name="privacy"),
    path('terms', views.terms, name="terms"),
    path('disclaimer', views.disclaimer, name="disclaimer"),
    path('pricing', views.pricing, name="pricing"),
    path('services', views.services, name="services"),
    path('membership', views.membership, name="membership"),
    path('register', views.register, name="register"),
]
