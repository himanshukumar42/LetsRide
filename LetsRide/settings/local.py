from LetsRide.settings.common import *
from LetsRide.utility.get_env import get_env_value
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

print("Local Settings")
SECRET_KEY = get_env_value('SECRET_KEY')
DEBUG = get_env_value('DEBUG')
ALLOWED_HOSTS = get_env_value('ALLOWED_HOSTS').split(' ')

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
