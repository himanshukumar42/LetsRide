from django.http import JsonResponse

def health_check(request): # noqa
    return JsonResponse({'health': 'ok'})
