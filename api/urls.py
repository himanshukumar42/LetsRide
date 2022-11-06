from api.views import common, accounts, rider, requester
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'login', accounts.LoginViewSet, basename='login')
router.register(r'sign-up', accounts.SignUpViewSet, basename='sign-up')
router.register(r'logout', accounts.LogoutViewSet, basename='logout')

urlpatterns = [
    path('', common.health_check, name='health_check'),

    # account
    path('', include(router.urls)),

    # rider
    path('rider/', rider.RiderListCreateAPIView.as_view(), name='rider_create'),
    path('rider/<int:pk>/get/', rider.RiderDetailAPIView.as_view(), name='rider_get'),
    path('rider/<int:pk>/update/', rider.RiderUpdateAPIView.as_view(), name='rider-update'),
    path('rider/<int:pk>/delete/', rider.RiderDeleteAPIView.as_view(), name='rider-delete'),
    path('riders/<int:pk>/', rider.RiderMixinView.as_view(), name='riders-get'),

    # requester
    path('requester/', requester.RequesterListCreateAPIView.as_view(), name='rider_create'),
    path('requester/<int:pk>/get/', requester.RequesterDetailAPIView.as_view(), name='rider_get'),
    path('requester/<int:pk>/update/', requester.RequesterUpdateAPIView.as_view(), name='rider-update'),
    path('requester/<int:pk>/delete/', requester.RequesterDeleteAPIView.as_view(), name='rider-delete'),
    path('requesters/<int:pk>/', requester.RequesterMixinView.as_view(), name='riders-get')
]
