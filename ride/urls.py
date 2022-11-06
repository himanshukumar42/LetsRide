from django.urls import path
from ride.views import common, rider, requester
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('health-check', common.health_check, name='health_check'),
    path('login/', common.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # rider
    path('', rider.RiderView.as_view(), name='riders'),
    path('rider/', rider.RiderView.as_view(), name='riders'),
    path('rider/<int:pk>/', rider.RiderDetail.as_view(), name='rider'),
    path('rider-create/', rider.RiderCreate.as_view(), name='rider-create'),
    path('rider-update/<int:pk>', rider.RiderUpdate.as_view(), name='rider-update'),
    path('rider-delete/<int:pk>', rider.RiderDelete.as_view(), name='rider-delete'),

    # requester
    path('', requester.RequesterView.as_view(), name='requesters'),
    path('requester/', requester.RequesterView.as_view(), name='requesters'),
    path('requester/<int:pk>/', requester.RequesterDetail.as_view(), name='requester'),
    path('requester-create/', requester.RequesterCreate.as_view(), name='requester-create'),
    path('requester-update/<int:pk>', requester.RequesterUpdate.as_view(), name='requester-update'),
    path('requester-delete/<int:pk>', requester.RequesterDelete.as_view(), name='requester-delete'),
]
