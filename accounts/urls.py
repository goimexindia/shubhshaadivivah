from . import views
from .views import *
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('eventinfo', views.eventinfo, name='eventinfo'),
    path('signup/', views.signup, name='signup'),
    path('eventsignup/', views.eventsignup, name='eventsignup'),
    path('success/', views.success, name='success'),
    path('handlesignup', views.handlesignup, name='handlesignup'),
    path('handlesignup1', views.handlesignup1, name='handlesignup1'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('profile', views.profile, name='profile'),
    path('profile1', views.profile1, name='profile1'),
    path('customer', views.customer, name='customer'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('profilepref', views.profilepref, name='profilepref'),
    path('familyvalues', views.familyvalues, name='familyvalues'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('shaadiprofile/<int:pk>/', views.shaadiprofile, name='shaadiprofile'),
]
