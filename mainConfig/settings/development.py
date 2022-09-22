
from .base import *

DEBUG = config('DEBUG')
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '*'
    ]



# Project APP 
INSTALLED_APPS += [
    'structure.accounts.apps.AccountsConfig',
    'structure.company.apps.CompanyConfig'
]

# Third party APP
INSTALLED_APPS += [
    'rest_framework',
    'drf_yasg',
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


'''
Custom Settings files 
'''

AUTH_USER_MODEL = 'accounts.User'