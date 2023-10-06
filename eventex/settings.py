"""
Django settings for eventex project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import pymysql
from pathlib import Path
from decouple import config, Csv
from dj_database_url import parse as dburl
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps Thirds
    'test_without_migrations',
    'django_extensions',
    # My apps
    'eventex.core',
    'eventex.subscriptions.apps.SubscriptionsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eventex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eventex.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


if DEBUG:
    default_dburl = 'sqlite:///' + str(BASE_DIR / 'db.sqlite3')
    DATABASES = {
        'default': config('DATABASE_URL', default=default_dburl, cast=dburl),  
    }
else:
    # Configurações
    username = config('PLANETSCALE_DB_USERNAME')
    password = config('PLANETSCALE_DB_PASSWORD')
    host = config('PLANETSCALE_DB_HOST')
    db = config('PLANETSCALE_DB')
    # Database
    database_url = f'mysql://{username}:{password}@{host}/{db}'
    print(database_url)
    #database_url = "mysql://" + str(config('PLANETSCALE_DB_USERNAME'))+":" + str(config('PLANETSCALE_DB_PASSWORD')) + "@" + str(config('PLANETSCALE_DB_HOST')) + "/" + str(config('PLANETSCALE_DB'))
    DATABASES = {
        'default': dburl(
            database_url, conn_max_age=600, ssl_require=True
        )
    }
    DATABASES['default']['OPTIONS']['charset'] = 'utf8mb4'
    del DATABASES['default']['OPTIONS']['sslmode']
    DATABASES['default']['OPTIONS']['ssl'] =  {'ca': os.environ.get('PLANETSCALE_SSL_CERT_PATH')}
    print(DATABASES)


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'static')

MEDIA_URL = 'img/'
MEDIA_ROOT = str(BASE_DIR / 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FROM_EMAIL = 'noobemforma@gmail.com'

# Email Configuration
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_USE_SSL = config('EMAIL_USE_SSL', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
