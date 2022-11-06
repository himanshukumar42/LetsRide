from rest_framework import serializers
from ride.models import Rider, Requester


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = '__all__'


class RequesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requester
        fields = '__all__'
