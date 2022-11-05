import os
from django.core.exceptions import ImproperlyConfigured
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def get_env_value(env_variable):
    try:
        return os.environ.get(env_variable)
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(env_variable)
        raise ImproperlyConfigured(error_msg)
