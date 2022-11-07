from rest_framework.permissions import AllowAny
from ride.views import common, rider, requester
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='LetsRide API',
        default_version='v1',
        description='LetsRide Description',
        terms_of_service='https://github.com/himanshukumar42/LetsRide',
        contact=openapi.Contact(email='kumarhimanshu250798@gmail.com'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=[AllowAny]
)

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

    # swagger
    re_path(r'^v1/', include('api.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'), # noqa
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # noqa
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-doc'),  # noqa
]
