from .base import *
import dj_database_url

DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

DEBUG = False

SECRET_KEY = os.environ.get('ADVERTISING_BACKEND__SECRET_KET')

CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?localhost:\d+$',)

ALLOWED_HOSTS = ['valid_adres_should_be_here.herokuapp.com']