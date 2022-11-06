from LetsRide.utility.messages import ERROR_CODE, SUCCESS_CODE
from LetsRide.utility.constant import SPECIAL_CHARACTERS, INT_NUMBER
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework import serializers, status
import re

USER = get_user_model()


class ApiResponse:
    """ Custom API Response class """
    is_success = False
    is_error = False
    is_validation_error = False

    def custom_response(self, message=None, data=None, response_status=status.HTTP_200_OK, allow_empty_list=False):
        self.is_success = True
        if allow_empty_list:
            response = Response({'detail': message if message else SUCCESS_CODE['3000'],
                                 'data': data}, status=response_status)
        else:
            response = Response({'detail': message if message else SUCCESS_CODE['3000'],
                                 'data': data if data else {}}, status=response_status)
        return response

    @staticmethod
    def _get_validate_error_string(errors):
        detail_error = list(errors.values())[0]
        if isinstance(detail_error, list):
            detail_error = detail_error[0]
        if isinstance(detail_error, dict):
            detail_error = list(detail_error.values())[0]
        return detail_error

    def custom_error(self, message=None, response_status=status.HTTP_400_BAD_REQUEST):
        self.is_error = True
        error = message
        if isinstance(message, str):
            error = None
        else:
            message = self._get_validate_error_string(error)
        return Response({'detail': message, 'error': error}, status=response_status)

    def custom_validation_error(self, message=None):
        self.is_validation_error = True
        raise ValidationError({'detail': message})


def validate_password(password):
    """
    Method to validate account password
    """
    regex = re.compile(SPECIAL_CHARACTERS)
    if len(password) < INT_NUMBER['EIGHT']:
        raise serializers.ValidationError(
            ERROR_CODE['password']['character_limit'])
    elif re.search('\\d', password) is None:
        raise serializers.ValidationError(
            ERROR_CODE['password']['number_required'])
    elif re.search('[A-Z]', password) is None:
        raise serializers.ValidationError(
            ERROR_CODE['password']['capital_letter_required'])
    elif re.search('[a-z]', password) is None:
        raise serializers.ValidationError(
            ERROR_CODE['password']['small_letter_required'])
    elif regex.search(password) is None:
        raise serializers.ValidationError(
            ERROR_CODE['password']['special_character_required'])
    elif ' ' in password:
        raise serializers.ValidationError(
            ERROR_CODE['global_error']['not_allowed'].format(
                "spaces", "password"))

    return password


def validate_name(names):
    for name in names:
        if re.search('\\d', name):
            raise serializers.ValidationError(
                ERROR_CODE['global_error']['not_allowed'].format(
                    "numbers", "both first name and last name"
                )
            )


def get_message(obj):
    result = None
    if isinstance(obj, list):
        if isinstance(obj[0], list):
            result = get_message(obj[0][0])
        elif isinstance(obj[0], dict):
            result = get_message(obj[0].items()[0])
        else:
            result = obj[0]

    elif isinstance(obj, dict):
        dict_item = list(obj.items())
        if isinstance(dict_item, dict):
            result = get_message(dict_item.items())
        elif isinstance(dict_item, list):
            result = get_message(dict_item[0])
        else:
            result = dict_item

    elif isinstance(obj, tuple):
        result = get_message(obj[1])

    return result


def get_access_token(user):
    print(user)


def expire_previous_tokens(user_id):
    print(user_id)


def logout(user_id, access_token):
    """ Remove access_token and registration_token """
    try:
        user = User.objects.get(pk=user_id)
        print(user)
        print("logout")
        print("access_token: ", access_token)
    except USER.DoesNotExist:
        pass
