import os
from django.conf import settings

import django

from django_loguru.configs import DEFAULTS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings.configure(
    SECRET_KEY = "notasecret",
    BASE_DIR = BASE_DIR,
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        "django_loguru",
        "tests"
    ],
    ALLOWED_HOSTS=['*'],
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    },
    TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates"}],
    ROOT_URLCONF = "tests.urls",
    SITE_ID=1,
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        "django_loguru.middleware.DjangoLoguruMiddleware"
    ],
    DJANGO_LOGGING_MIDDLEWARE = DEFAULTS,
    APPEND_SLASH=False,
    STATIC_URL = '/static/'
)

django.setup()