from django.urls import path
from . import views
from .views import EcomerceView

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('productcontact', views.productcontact, name="productcontact"),
    path('ellite', views.ellite, name="ellite"),
    path('about', views.about, name="about"),
    path("product", views.EcomerceView, name="product"),
    path("product1", views.EcomerceView1, name="product1"),
    path("product2", views.EcomerceView2, name="product2"),
    path("product3", views.EcomerceView3, name="product3"),
    path('faq', views.faq, name="faq"),
    path('privacy', views.privacy, name="privacy"),
    path('terms', views.terms, name="terms"),
    path('disclaimer', views.disclaimer, name="disclaimer"),
    path('secure', views.secure, name="secure"),
    path('pricing', views.pricing, name="pricing"),
    path('services', views.services, name="services"),
    path('membership', views.membership, name="membership"),
    path('catsearch/', views.catsearch, name='cat-search'),
    path('register', views.register, name="register"),

]
