from django.http import JsonResponse
from rest_framework import generics, mixins, permissions, authentication

from ride.models import Rider
from ride.serializers import RideSerializer, RequesterSerializer


def health_check(request, *args, **kwargs):
    return JsonResponse({"Health": "Ok"})


class RiderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rider.objects.all()
    serializer_class = RideSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description')
        if description is None:
            description = 'Default Description for ' + name
        serializer.save(description=description)


class RiderUpdateAPIView(generics.UpdateAPIView):
    queryset = Rider.objects.all()
    serializer_class = RideSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.description:
            instance.description = instance.name


class RiderDeleteAPIView(generics.DestroyAPIView):
    queryset = Rider.objects.all()
    serializer_class = RideSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


class RiderDetailAPIView(generics.RetrieveAPIView):
    queryset = Rider.objects.all()
    serializer_class = RideSerializer
    lookup_field = 'pk'


class RiderMixinView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin
):

    queryset = Rider.objects.all()
    serializer_class = RideSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
