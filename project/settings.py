import os
from dotenv import load_dotenv


load_dotenv()
DATABASES = {
    'default': {
        'ENGINE': os.environ['DATABASES_ENGINE'],
        'HOST': os.environ['DATABASES_HOST'],
        'PORT': os.environ['DATABASES_PORT'],
        'NAME': os.environ['DATABASES_NAME'],
        'USER': os.environ['DATABASES_USER'],
        'PASSWORD': os.environ['DATABASES_PASSWORD'],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = os.environ['LANGUAGE_CODE']

TIME_ZONE = os.environ['TIME_ZONE']

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
