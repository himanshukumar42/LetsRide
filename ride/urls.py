from django.urls import path
from .views import health_check, RiderView, RiderDetail, RiderCreate, RiderUpdate, RiderDelete, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('health-check', health_check, name='health_check'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', RiderView.as_view(), name='riders'),
    path('rider/', RiderView.as_view(), name='riders'),
    path('rider/<int:pk>/', RiderDetail.as_view(), name='rider'),
    path('rider-create/', RiderCreate.as_view(), name='rider-create'),
    path('rider-update/<int:pk>', RiderUpdate.as_view(), name='rider-update'),
    path('rider-delete/<int:pk>', RiderDelete.as_view(), name='rider-delete'),
]
