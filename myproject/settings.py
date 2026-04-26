import os
from pathlib import Path

# 1. Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Security
SECRET_KEY = 'django-insecure-%yd-i3#a-ywff0@u31n+n72a-q*@qo%+4(a$us#t0v(8tujfc-'
DEBUG = True
ALLOWED_HOSTS = ['ai-learning-path-7l4x.onrender.com', 'localhost', '127.0.0.1', '*']

# 3. App Definitions
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'core',
    'corsheaders',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

# 4. Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

# 5. Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core' / 'templates'], 
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

WSGI_APPLICATION = 'myproject.wsgi.application'

import dj_database_url

# 6. Database
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'), conn_max_age=600)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# 7. Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 8. Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 9. Static Files
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'core' / 'static']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 10. Authentication Settings
SITE_ID = 1
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/login/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/login/'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# 11. Social Account Providers
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': True
    }
}
SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_PROMPT_ON_LOGOUT = False

# 12. Security / CORS
CORS_ALLOW_ALL_ORIGINS = True 
CSRF_TRUSTED_ORIGINS = [
    'https://ai-learning-path-3yon.onrender.com',
    'https://ai-learning-path-6.onrender.com',
    'https://ai-learning-path-a9ws.vercel.app',
    'http://127.0.0.1:8000',
    'http://localhost:8000'
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Session Settings
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 300 
SESSION_SAVE_EVERY_REQUEST = True
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'bchandar295@gmail.com' 
EMAIL_HOST_PASSWORD = 'bhlxmulqcizwzddq' 
DEFAULT_FROM_EMAIL = 'AI Learning <bchandar295@gmail.com>'