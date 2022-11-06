from LetsRide.utility.messages import ERROR_CODE
from LetsRide.utility.constant import SPECIAL_CHARACTERS, INT_NUMBER
from rest_framework import serializers
import re


def get_access_token(user):
    print(user)


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
