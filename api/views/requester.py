from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework import generics, mixins
from ride.serializers.serializers import RequesterSerializer
from ride.models import Requester


class RequesterListCreateAPIView(generics.ListCreateAPIView):
    queryset = Requester.objects.all()
    serializer_class = RequesterSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        name = serializer.validated_data.get('user')
        print('User:- ', name)
        description = serializer.validated_data.get('description')
        if description is None:
            description = 'Default Description '
        serializer.save(description=description)


class RequesterUpdateAPIView(generics.UpdateAPIView):
    queryset = Requester.objects.all()
    serializer_class = RequesterSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.description:
            instance.description = instance.name


class RequesterDeleteAPIView(generics.DestroyAPIView):
    queryset = Requester.objects.all()
    serializer_class = RequesterSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


class RequesterDetailAPIView(generics.RetrieveAPIView):
    queryset = Requester.objects.all()
    serializer_class = RequesterSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'


class RequesterMixinView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin
):

    queryset = Requester.objects.all()
    serializer_class = RequesterSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
