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
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('social-auth/', include('social_django.urls', namespace="social")),
]
