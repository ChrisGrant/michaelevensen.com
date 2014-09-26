"""
Django settings for michaelevensen project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# for HTML and XHTML
# DEFAULT_CONTENT_TYPE = 'application/xhtml+xml'


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wp4uz!&&c5txut!9%o&*6ac=+^@#+s70_(n#)tlm+ib9qb2q1+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Application definition

INSTALLED_APPS = (
    'django_summernote',
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'portfolio',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'michaelevensen.urls'

WSGI_APPLICATION = 'michaelevensen.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
 	'ENGINE': 'django.db.backends.sqlite3',
	'NAME':	os.path.join(BASE_DIR, 'db.michaelevensen')
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = '/Users/michaelevensen/Sites/michaelevensen.com/www/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '/Users/michaelevensen/Sites/michaelevensen.com/www/static/'),
)

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = '/Users/michaelevensen/Sites/michaelevensen.com/www/media/'
