from django.urls import path
from .views import health_check, RiderView, RiderDetail, RiderCreate


urlpatterns = [
    path('', health_check, name='health_check'),
    path('rider/', RiderView.as_view(), name='riders'),
    path('rider/<int:pk>/', RiderDetail.as_view(), name='rider'),
    path('rider-create/', RiderCreate.as_view(), name='rider-create'),
]
