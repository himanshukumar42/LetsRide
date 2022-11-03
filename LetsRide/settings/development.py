from LetsRide.settings.common import *
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get('SECRET_KEY', 'development')
DEBUG = os.environ.get('DEBUG', False)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT')
    }
}
