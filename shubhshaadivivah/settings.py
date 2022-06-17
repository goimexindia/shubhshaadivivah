import os
from pathlib import Path
from decouple import config, Csv
from .sec import *
from datetime import timedelta
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'ijo8611y6x@3b-+(k&5z=xj$u6olrwga^b#jp_syw+6fuelx^8'

DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
ALLOWED_HOSTS = [www.shubhshaadivivah.com, shubhshaadivivah.com, 167.71.236.18]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vivah.apps.VivahConfig',
    'socials.apps.SocialsConfig',
    'accounts.apps.AccountsConfig',
    'crispy_forms',
    'django.contrib.sites',
    'storages',
    # 3rd party
    "allauth",  # new
    "allauth.account",  # new
    "allauth.socialaccount",  # new
    # social providers
    "allauth.socialaccount.providers.github",  # new
    "allauth.socialaccount.providers.twitter",  # new
    "allauth.socialaccount.providers.google",  # new
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.linkedin",
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_countries',
    'django_filters',
    'ckeditor',
    'django.contrib.sitemaps',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auto_logout.middleware.auto_logout',
]

ROOT_URLCONF = 'shubhshaadivivah.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'shubhshaadivivah.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
if DEBUG:
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
else:
  STATIC_ROOT = os.path.join(BASE_DIR, 'static')



GOOGLE_RECAPTCHA_SITE_KEY = '6Ld0N3wcAAAAAHHxBYv_044U5W4Gqp6nfA2yGF89'
GOOGLE_RECAPTCHA_SECRET_KEY = '6Ld0N3wcAAAAAD42aciPXinfohM5K5R96c9aa4f-'

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGOUT_ON_GET = True

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'

SOCIAL_AUTH_FACEBOOK_KEY = '554900665801603'
SOCIAL_AUTH_FACEBOOK_SECRET = '3e60de109bc4dd451a30c749591b54eb'
# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from facebook. Email is not sent by default, to get it, you must request the email permission:
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# S3 BUCKETS CONFIG
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_HOST = 'us-east-2'  # change to your region
S3_USE_SIGV4 = True

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#AUTO_LOGOUT = {'IDLE_TIME': 600}  # logout after 10 minutes of downtime

#AUTO_LOGOUT = {
#    'SESSION_TIME': 3600,
#    'MESSAGE': 'The session has expired. Please login again to continue.',
#}

AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=50),
    'SESSION_TIME': timedelta(minutes=180),
    'MESSAGE': 'The session has expired. Please login again to continue.',
}

CKEDITOR_CONFIGS = {
    # django-ckeditor defaults
    'default': {
        # Editor Width Adaptation
        'width': 'auto',
        'height': '250px',
        # tab key conversion space number
        'tabSpaces': 4,
        # Toolbar Style
        'toolbar': 'Custom',
        # Toolbar buttons
        'toolbar_Custom': [
            # Emotional Code Block
            ['Smiley', 'CodeSnippet'],
            # Font Style
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            # Font color
            ['TextColor', 'BGColor'],
        ],
        # Add Code Block Plug-ins
        'extraPlugins': ','.join(['codesnippet']),
    }
}

DJOSER = {
    "USER_ID_FIELD": "username",
    "LOGIN_FIELD": "email",
    "SEND_ACTIVATION_EMAIL": True,
    "ACTIVATION_URL": "activate/{uid}/{token}",
    'SERIALIZERS': {
        'token_create': 'apps.accounts.serializers.CustomTokenCreateSerializer',
    },
}


EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'noreply<no_reply@domain.com>'

