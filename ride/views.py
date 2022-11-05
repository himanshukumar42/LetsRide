from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import Rider


def health_check(request): # noqa
    return HttpResponse('<h1>Ride App Health Check Ok</h1>')


class CustomLoginView(LoginView):
    template_name = 'ride/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('riders')


class RiderView(ListView):
    model = Rider
    context_object_name = 'riders'
    template_name = 'ride/riders.html'


class RiderDetail(DetailView):
    model = Rider
    context_object_name = 'rider'
    template_name = 'ride/rider.html'


class RiderCreate(CreateView):
    model = Rider
    fields = '__all__'
    success_url = reverse_lazy('riders')


class RiderUpdate(UpdateView):
    model = Rider
    fields = '__all__'
    success_url = reverse_lazy('riders')


class RiderDelete(DeleteView):
    model = Rider
    fields = '__all__'
    success_url = reverse_lazy('riders')
