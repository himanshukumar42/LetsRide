from LetsRide.settings.common import *
from LetsRide.utility.request_response import get_env_value
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

print("Production Settings")
SECRET_KEY = get_env_value('SECRET_KEY')
DEBUG = get_env_value('DEBUG')
ALLOWED_HOSTS = get_env_value('ALLOWED_HOSTS').split(' ')
DATABASE_URL = get_env_value('DATABASE_URL')

DATABASES = {
    'default': {
        'ENGINE': get_env_value('DB_ENGINE'),
        'NAME': get_env_value('DB_NAME'),
        'USER': get_env_value('DB_USER'),
        'PASSWORD': get_env_value('DB_PASSWORD'),
        'HOST': get_env_value('DB_HOST'),
        'PORT': get_env_value('DB_PORT')
    }
}
