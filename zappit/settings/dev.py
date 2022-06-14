from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-q^!iub^7m@a^w$+g2%5o!!o)sc3s=plu6j(4gl@6%a0@izc7tu'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vote',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': 'Arun@7708',
        'PORT' : '5432'
    }
}