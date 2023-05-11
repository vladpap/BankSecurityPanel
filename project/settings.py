import os
from environs import Env


env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': env.str('DATABASES_ENGINE', default='django.db.backends.postgresql_psycopg2'),
        'HOST': env.str('DATABASES_HOST', default=''),
        'PORT': env.int('DATABASES_PORT', default=0),
        'NAME': env.str('DATABASES_NAME', default=''),
        'USER': env.str('DATABASES_USER', default=''),
        'PASSWORD': env.str('DATABASES_PASSWORD', default=''),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('SECRET_KEY', default='My secret Key')

DEBUG = env.str('DEBUG', default='True').lower() == 'true'

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = env.str('LANGUAGE_CODE', default='ru-ru')

TIME_ZONE = env.str('TIME_ZONE', default='Europe/Moscow')

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
