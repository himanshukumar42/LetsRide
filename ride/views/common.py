from ride.serializers.auth_serializers import UserRegistrationSerializer
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.http import HttpResponse
from django.urls import reverse_lazy


def health_check(request): # noqa
    return HttpResponse('<h1>Ride App Health Check Ok</h1>')


class CustomLoginView(LoginView):
    template_name = 'ride/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('riders')


class SignUpViewSet(viewsets.ModelViewSet):
    """ Signup ViewSer for customers """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    http_method_names = ('post', )