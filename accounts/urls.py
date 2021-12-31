from . import views
from .views import *
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name='login'),
    path('insert', views.insert, name='insert'),
    path('logout', views.logout, name='logout'),
    path('eventinfo', views.eventinfo, name='eventinfo'),
    path('signup/', views.signup, name='signup'),
    path('eventsignup/', views.eventsignup, name='eventsignup'),
    path('success/', views.success, name='success'),
    path('handlesignup', views.handlesignup, name='handlesignup'),
    path('handlesignup1', views.handlesignup1, name='handlesignup1'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('profile', views.profile, name='profile'),
    path('postdetails', views.postdetails, name='postdetails'),
    path('profile1', views.profile1, name='profile1'),
    path('customer', views.customer, name='customer'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('profilepref', views.profilepref, name='profilepref'),
    path('familyvalues', views.familyvalues, name='familyvalues'),
    path('socialss-auth/', include('social_django.urls', namespace="socialss")),
    path('shaadiprofile/<int:pk>/', views.shaadiprofile, name='shaadiprofile'),
    path('prodcomment/<int:pk>/', views.prodcomment, name='prodcomment'),
    path('like/<int:pk>', views.like, name='like'),
    path('notification/<int:notification_pk>/thread/<int:object_pk>', ThreadNotification.as_view(),
         name='thread-notification'),
    path('notification/delete/<int:notification_pk>', RemoveNotification.as_view(), name='notification-delete'),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>', FollowNotification.as_view(),
         name='follow-notification'),
    path('notification/<int:notification_pk>',
         PostNotification.as_view(), name='post-notification'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('passwrd/', PasswordsChangeView.as_view(), name='passwrd')
]
