from LetsRide.settings.common import *
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

Print("Staging Settings")
SECRET_KEY = os.environ.get('SECRET_KEY', 'staging-secret')
DEBUG = False
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')
DATABASE_URL = os.environ.get('DATABASE_URL')

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
