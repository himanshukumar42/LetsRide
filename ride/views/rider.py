from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ride.models import Rider


class RiderView(LoginRequiredMixin, ListView):
    model = Rider
    context_object_name = 'riders'
    template_name = 'ride/riders.html'


class RiderDetail(LoginRequiredMixin, DetailView):
    model = Rider
    context_object_name = 'rider'
    template_name = 'ride/rider.html'


class RiderCreate(LoginRequiredMixin, CreateView):
    model = Rider
    fields = '__all__'
    success_url = reverse_lazy('riders')


class RiderUpdate(LoginRequiredMixin, UpdateView):
    model = Rider
    fields = '__all__'
    success_url = reverse_lazy('riders')


class RiderDelete(LoginRequiredMixin, DeleteView):
    model = Rider
    fields = '__all__'
    success_url = reverse_lazy('riders')

