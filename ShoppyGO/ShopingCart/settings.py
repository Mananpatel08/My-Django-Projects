import os
from pathlib import Path
from decouple import config, Csv
from dotenv import load_dotenv
from .adminpanel import JAZZMIN_SETTINGS, JAZZMIN_UI_TWEAKS

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env-example'))

# DEBUG = config('DEBUG', default=True, cast=bool)
# SECRET_KEY = config('SECRET_KEY')

DEBUG = os.getenv('DEBUG', 'False') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY')


ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'ShoppyGo',
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

CORS_ALLOWED_ORIGINS = [
    "https://www.paypal.com",  
    "https://www.sandbox.paypal.com", 
    "http://127.0.0.1:8000",  
]

ROOT_URLCONF = 'ShopingCart.urls'

SESSION_COOKIE_NAME = "website_session"  
SESSION_COOKIE_AGE = 86400  

ADMIN_SESSION_COOKIE_NAME = "admin_session"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR , 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'ShoppyGo.cart_context.cart_count',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ShopingCart.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  

LOGIN_URL = '/accounts/login'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


AUTH_USER_MODEL = 'ShoppyGo.CustomUser'  

# ======================================================
# STRIPE PAYMENT
# ======================================================

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')