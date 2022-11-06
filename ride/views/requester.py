from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ride.models import Requester


class RequesterView(LoginRequiredMixin, ListView):
    model = Requester
    context_object_name = 'riders'
    template_name = 'ride/riders.html'


class RequesterDetail(LoginRequiredMixin, DetailView):
    model = Requester
    context_object_name = 'rider'
    template_name = 'ride/rider.html'


class RequesterCreate(LoginRequiredMixin, CreateView):
    model = Requester
    fields = '__all__'
    success_url = reverse_lazy('riders')


class RequesterUpdate(LoginRequiredMixin, UpdateView):
    model = Requester
    fields = '__all__'
    success_url = reverse_lazy('riders')


class RequesterDelete(LoginRequiredMixin, DeleteView):
    model = Requester
    fields = '__all__'
    success_url = reverse_lazy('riders')

