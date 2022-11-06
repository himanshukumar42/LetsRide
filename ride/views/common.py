from django.contrib.auth.views import LoginView
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
