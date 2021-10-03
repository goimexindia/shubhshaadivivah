from . import views
from .views import *
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('social-auth/', include('social_django.urls', namespace="social")),
]
