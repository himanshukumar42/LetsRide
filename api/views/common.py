from rest_framework.pagination import PageNumberPagination
from ride.models import Rider, Requester
from rest_framework import generics
from django.forms.models import model_to_dict
from django.db.models import Q
from django.http import JsonResponse


def health_check(request):  # noqa
    return JsonResponse({'health': 'ok'})


class RiderRequesterMatchAPIView(generics.GenericAPIView):
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        request_data = request.data
        print(request_data)

        sort_by_date = bool(request_data.get('sort_by_date', None))
        status = request_data.get('status', None)
        asset_type = request_data.get('asset_type', None)

        requesters = Requester.objects.all().extra(
            tables=("ride_rider",),
            where=('''ride_rider.from_location=ride_requester.from_location AND
                   ride_rider.to_location=ride_requester.to_location AND
                   ride_rider.date_time=ride_requester.date_time''',),
        )
        if status is not None:
            requesters = requesters.filter(Q(status=status))
        if asset_type is not None:
            requesters = requesters.filter(Q(asset_type=asset_type))
        if sort_by_date:
            print('reached sort by date')
            requesters.order_by('date_time')

        data = []
        for requester in requesters:
            data.append(model_to_dict(requester))

        paginator = PageNumberPagination()
        p = paginator.paginate_queryset(queryset=requesters, request=request)
        return paginator.get_paginated_response(data)
