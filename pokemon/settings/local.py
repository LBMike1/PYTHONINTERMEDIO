
from .base import *  # noqa: F403

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xdyfkcj64i@(#a$hevbc0l*e(!6**kfxwnadkzlsce5kha-=bc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# Permite crear una lista para indicar que IP's se pueden conectar a nuestro aplicativo.
# * : Permite que cualquier IP se pueda conectar.

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_poke',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',  # 127.0.0.1
        'PORT': 5432
    }
}

"""
-> Base de Datos relacionales:
 - mysql
 - postgresql
 - sqlserver
 - RDS (AWS)

-> Base de Datos no relaciones:
- firebase
- mongo DB
- Dynamo DB (AWS)
"""

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIR = [
    BASE_DIR / 'static',  # noqa: F405
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # noqa: F405
