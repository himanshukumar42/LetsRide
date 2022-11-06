from LetsRide.utility.helpers import get_access_token, validate_password, validate_name
from LetsRide.utility.validator import USER_UNIQUE_FIELD_VALIDATOR
from LetsRide.utility.messages import ERROR_CODE, ErrorManager
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.exceptions import AuthenticationFailed
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.utils.encoding import force_str
from rest_framework import serializers
from django.db.models import Q


class LoginSerializer(serializers.ModelSerializer):
    """ Serializer for login process. """

    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=True,
                                   error_messages={"blank": ErrorManager().get_blank_field_message('email')}
                                   )
    password = serializers.CharField(max_length=100, required=True, trim_whitespace=False,
                                     error_messages={"blank": ErrorManager().get_blank_field_message('password')}
                                     )
    token = serializers.SerializerMethodField(required=False)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'token')

    def validate_data(self, validated_data):
        email = validated_data.get('email', None)
        password = validated_data.get('password', None)

        user = None
        try:
            user = User.objects.get(Q(email__iexact=email) | Q(username__iexact=email))
        except User.DoesNotExist:
            self.custom_validate_error(message=ERROR_CODE['user']['not_exist'])

        if not User.is_active:
            self.custom_validate_error(message=ERROR_CODE['login']['deactivated'])

        if not user.check_password(password):
            self.custom_validate_error(
                message=ERROR_CODE['login']['invalid_credential']
            )

        return user

    def create(self, validated_data):
        user = self.validate_data(validated_data)
        return user

    @staticmethod
    def get_token(obj):
        return get_access_token(obj)

    def to_representation(self, instance):
        attr = super(LoginSerializer, self).to_representation(instance)
        attr.pop('password')
        return attr

    def custom_validate_error(self, message):
        pass


class UserRegistrationSerializer(serializers.ModelSerializer):
    """ Serializer for User Registration """

    first_name = serializers.CharField(required=True, max_length=50,
                                       error_messages={
                                           'blank': ErrorManager().get_blank_field_message('first_name'),
                                           'max_length': ErrorManager().get_maximum_limit_message('first_name', '50')
                                       })
    last_name = serializers.CharField(required=True, max_length=50,
                                      error_messages={
                                          'blank': ErrorManager().get_blank_field_message('last_name'),
                                          'max_length': ErrorManager().get_maximum_limit_message('last_name', '50')
                                      })
    email = serializers.EmailField(required=True, max_length=15, min_length=5,
                                   error_messages={
                                       'blank': ErrorManager().get_blank_field_message('email'),
                                       'max_length': ErrorManager().get_maximum_limit_message('email', '150'),
                                       'min_length': ErrorManager().get_minimum_limit_message('email', '5'),
                                       'invalid': ERROR_CODE['sign_up']['invalid_email']
                                   })
    password = serializers.CharField(required=True, max_length=15, min_length=8,
                                     error_messages={
                                         'blank': ErrorManager().get_blank_field_message('password'),
                                         'min_length': ErrorManager().get_minimum_limit_message('password', '8'),
                                         'max_length': ErrorManager().get_maximum_limit_message('password', '15')
                                     })
    confirm_password = serializers.CharField(required=True, max_length=15, min_length=8, error_messages={
        'blank': ErrorManager().get_blank_field_message('password'),
        'min_length': ErrorManager().get_minimum_limit_message('password', '8'),
        'max_length': ErrorManager().get_maximum_limit_message('password', '15'),
    }, read_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'confirm_password')
        validators = USER_UNIQUE_FIELD_VALIDATOR

    @staticmethod
    def validate_email(value):
        return value.lower()

    @staticmethod
    def validate_password(password):
        return validate_password(password)

    def validate(self, data):
        if data.get('password') != self.context.get('confirm_password'):
            raise serializers.ValidationError(
                ERROR_CODE['password']['confirm_password_invalid']
            )
        validate_name([data.get('first_name'), data.get('last_name')])

        return data

    def create(self, validated_data):
        validated_data['is_active'] = True
        validated_data['username'] = validated_data['email']
        instance = User.objects.create_user(**validated_data)
        instance.save()
        return instance

    def to_representation(self, instance):
        rep = super(UserRegistrationSerializer, self).to_representation(instance)
        rep.pop('password')
        return rep


class UserForgotPasswordSerializer(serializers.ModelSerializer):
    """ Forgot Password Serializer """

    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']


class SetNewResetPasswordSerializer(serializers.ModelSerializer):
    """ Reset Password Serializer """

    password = serializers.CharField(min_length=6, max_length=20, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uid64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uid64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uid64 = attrs.get('uid64')

            user_id = force_str(urlsafe_base64_decode(uid64))
            user = User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('the reset link is invalid', 401)

            user.set_password(password)
            user.save()

        except Exception as e:
            raise AuthenticationFailed(f'exception occurred: {e}', 401)

        return super().validate(attrs)
