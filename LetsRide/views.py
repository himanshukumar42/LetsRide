from django.http import HttpResponse
from django.shortcuts import render


def health_check(request):
    return HttpResponse('<h1>Health Check Ok</h1>')


def index(request):
    return render(request, 'index.html')


