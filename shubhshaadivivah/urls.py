from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'ShubhShaadiVivah  Administration'
admin.site.site_title = 'ShubhShaadiVivah Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vivah.urls')),
    path('socials/', include('socials.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path('accounts/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
