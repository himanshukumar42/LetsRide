#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from LetsRide.utility.request_response import get_env_value
import os
import sys


def main():
    """Run administrative tasks."""
    print('Environment :- ', get_env_value('ENV'))
    if get_env_value('ENV') == 'local':
        print("Reaching here")
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LetsRide.settings.local')
    elif get_env_value('ENV') == 'development':
        print("idhar nahi aane ka")
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LetsRide.settings.development')
    elif get_env_value('ENV') == 'staging':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LetsRide.settings.staging')
    elif get_env_value('ENV') == 'production':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LetsRide.settings.production')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LetsRide.settings.local')
        print("Invalid environment variable")
    try:
        from django.core.management import execute_from_command_line
        print("+++++++++++++++ hoo lala lla")
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    print("i am here now")
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    main()
