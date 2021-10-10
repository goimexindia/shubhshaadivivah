from . import views
from .views import *
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('handlesignup', views.handlesignup, name='handlesignup'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('profile', views.profile, name='profile'),
    path('profile1', views.profile1, name='profile1'),
    path('profilepref', views.profilepref, name='profilepref'),
    path('social-auth/', include('social_django.urls', namespace="social")),
]
