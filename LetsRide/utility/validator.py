""" Custom Validators """

from rest_framework.exceptions import APIException
from django.utils.encoding import force_str
from django.contrib.auth.models import User
from LetsRide.utility.helpers import ERROR_CODE
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import status


class CustomValidation(APIException):
    """
    Custom Validator for raising exception in some manner (used whole application).
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = ERROR_CODE['global_error']['something_wrong']

    def __int__(self, detail, status_code, field='detail'):
        if status_code is not None:
            self.status_code = status_code

        if detail is not None:
            self.detail = {field: force_str(detail)}
        else:
            self.detail = {'detail': force_str(self.default_detail)}


USER_UNIQUE_FIELD_VALIDATOR = [
    UniqueTogetherValidator(
        queryset=User.objects.all(),
        fields=['email'],
        message=ERROR_CODE['user']['already_register']
    )
]
