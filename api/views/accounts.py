from ride.serializers.auth_serializers import LoginSerializer, \
    UserRegistrationSerializer, UserForgotPasswordSerializer, SetNewResetPasswordSerializer, LogoutSerializer
from LetsRide.utility.messages import SUCCESS_CODE
from LetsRide.utility.helpers import ApiResponse, logout, get_message
from rest_framework.permissions import IsAuthenticated
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from LetsRide.settings.common import EMAIL_HOST_USER
from django.urls import reverse
from django.http import JsonResponse
from rest_framework import viewsets, generics, status


class LoginViewSet(viewsets.ModelViewSet, ApiResponse):
    """ Login Model ViewSet"""

    serializer_class = LoginSerializer
    queryset = User.objects.all()
    http_method_names = ['post']

    def get_serializer_context(self):
        return {'request': self.request}


class LogoutViewSet(viewsets.GenericViewSet, ApiResponse):
    """ Logout ViewSet class """
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer
    http_method_names = ('post',)

    def create(self, request):
        logout(request.user.id, request.META['HTTP_AUTHORIZATION'].split(' ')[1])
        return self.custom_response(
            message=SUCCESS_CODE['user']['log_out'],
            data=None,
            response_status=status.HTTP_200_OK
        )


class SignUpViewSet(viewsets.ModelViewSet, ApiResponse):
    """ SignUp ViewSet class """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    http_method_names = ('post', )

    def create(self, request, *args, **kwargs):
        user_create_serializer_instance = self.serializer_class(
            data=request.data,
            context={'confirm_password': request.data.get('confirm_password')}
        )
        if user_create_serializer_instance.is_valid():
            user_create_serializer_instance.save()
            return self.custom_response(
                SUCCESS_CODE['user']['registration_done'],
                user_create_serializer_instance.data,
                response_status=status.HTTP_201_CREATED
            )

        return self.custom_error(
            get_message(user_create_serializer_instance.errors),
            response_status=status.HTTP_400_BAD_REQUEST
        )


class UserForgotPassword(generics.GenericAPIView):
    """ User Forgot Password"""
    serializer_class = UserForgotPasswordSerializer

    def post(self, request):
        _ = self.serializer_class(data=request.data)
        email = request.data['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = 'localhost:8080/index.html#/new-password'
            reverse_relative_link = reverse(viewname='password_reset_confirm', kwargs={'uid64': uid64, 'token': token})
            relative_link = reverse_relative_link.replace('/', '_')
            absolute_url = f'http://{current_site}?token={relative_link}'
            email_body = 'Hi \n Use this link to reset your password \n' + absolute_url
            send_mail(
                subject='Reset your Password',
                message=email_body,
                from_email=EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False
            )
            return JsonResponse({'success': 'We have sent a link to reset password on your link'}, status=200)
        else:
            return JsonResponse({'message': 'User does not exists'}, status=400)


class VerifyUserForgotPassword(generics.GenericAPIView, ApiResponse):
    """ Verify User Forgot Password class """
    def get(self, request, uid64, token):
        try:
            print(self.request)
            request.data = None
            user_id = smart_str(urlsafe_base64_decode(uid64))
            user = User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return JsonResponse({'error': 'Token expired, request a new one'}, status=401)
            return JsonResponse({'success': True, 'message': 'credentials valid',
                                 'uid64': uid64, 'token': token}, status=200)
        except DjangoUnicodeDecodeError as e:
            print(e)
            if not PasswordResetTokenGenerator():
                return JsonResponse({'error': 'Token is not valid'}, status=401)


class ResetPassword(generics.GenericAPIView, ApiResponse):
    """ Reset Password class """
    serializer_class = SetNewResetPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return JsonResponse({'success': True, 'message': 'Password reset successfully'}, status=200)
