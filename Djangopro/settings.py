"""
Django settings for Djangopro project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bh%xclluyf5pai31l3zf6ss9kv7lfeqqcx*q+qc)7r$fw6h*=)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Application definition

INSTALLED_APPS = [
    'stme.apps.StmeConfig',
    'django_cleanup', # ลบไฟล์รูปภาพเดิม  #pip install django-cleanup
    'users.apps.UsersConfig', #6 ติดตั้ง app ของ user
    'crispy_forms', #6 ตัดตั้ง crispy_forms รูปแบบ css #pip install django-crispy-forms
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taggit', # pip3 install django-taggit #https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
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

ROOT_URLCONF = 'Djangopro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'stme/templates')]
        ,
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

WSGI_APPLICATION = 'Djangopro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us' # LANGUAGE_CODE = 'TH-th'

TIME_ZONE = 'Asia/Bangkok' #TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#pip install django-translations

#python manage.py migrate

# https://brew.sh/index_th # Homebrew mac os


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #8
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4' #6

LOGIN_REDIRECT_URL = 'stme-home'
LOGIN_URL = 'login' #7 เมื่อเข้าหน้า profile โดยไม่ได้ล็อกอิน จะถูกส่งไปตาม url = login

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#python manage.py sendtestemail vitor@example.com



