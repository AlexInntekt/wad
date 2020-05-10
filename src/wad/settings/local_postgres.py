from .base import *
import os 

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'waddb',
        'USER': 'waddbuser',
        'PASSWORD': 'start123',
        'HOST' : 'localhost',
        'PORT': '5432',
    }
}
