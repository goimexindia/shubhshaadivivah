from . import views
from .views import *
from django.urls import path, include

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('social-auth/', include('social_django.urls', namespace="social")),
]
