"""
Django settings for valentina project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django
from valentina.settings_conf import *
from valentina.version import APP_VERSION

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(BASE_DIR, 'output/')

LOGIN_REDIRECT_URL = 'validation'

STATIC_ROOT=os.path.join(BASE_DIR, 'static/')

ENV_FILE_URL_TEMPLATE = "https://github.com/awst-austria/qa4sm/blob/v{}/environment/qa4sm_env.yml"

# Application definition
INSTALLED_APPS = [
    'validator.apps.ValidatorConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
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

ROOT_URLCONF = 'valentina.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # include default django templates and widgets, see https://docs.djangoproject.com/en/2.1/ref/forms/renderers/#templatessetting
        'DIRS': [django.__path__[0] + '/forms/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'valentina.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.environ['QA4SM_DB_NAME'],
    'USER': os.environ['QA4SM_DB_USER'],
    'PASSWORD': os.environ['QA4SM_DB_PASSWORD'],
    'HOST': os.environ['QA4SM_DB_HOST'],
    'PORT': '',
    }
}

AUTH_USER_MODEL = 'validator.User'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-GB'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FORMAT_MODULE_PATH = [
    'validator.formats',
]

# Logging, see https://docs.djangoproject.com/en/2.1/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} {levelname} {module}:{funcName}: {message}',
            'style': '{',
            },
        },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'validator': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
#         'py.warnings': {
#             'handlers': ['file', 'console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
    },
}

## Security settings

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
#try:
#    CSRF_COOKIE_SECURE = not DEBUG
#except NameError:
#    CSRF_COOKIE_SECURE = True
# print("Running with CSRF_COOKIE_SECURE = {}".format(CSRF_COOKIE_SECURE))

PASSWORD_RESET_TIMEOUT_DAYS = 1