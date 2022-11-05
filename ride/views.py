from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Requester, Rider


def health_check(request): # noqa
    return HttpResponse('<h1>Ride App Health Check Ok</h1>')


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
