from rest_framework import serializers
from ride.models import Rider, Requester
from ride.models import TRAVEL_MEDIUM, ASSET_TYPE, ASSET_SENSITIVITY, STATUS


class RideSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
    from_location = serializers.CharField(max_length=150)
    to_location = serializers.CharField(max_length=150)
    date_time = serializers.DateTimeField()
    flexible_timing = serializers.BooleanField()
    travel_medium = serializers.ChoiceField(choices=TRAVEL_MEDIUM)
    assets_quantity = serializers.IntegerField()
    
    def create(self, validated_data):
        return Rider(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.from_location = validated_data.get('from_location', instance.from_location)
        instance.to_location = validated_data.get('to_location', instance.to_location)
        instance.date_time = validated_data.get('date_time', instance.date_time)
        instance.flexible_timing = validated_data.get('flexible_timing', instance.flexible_timing)
        instance.travel_medium = validated_data.get('travel_medium', instance.travel_medium)
        instance.assets_quantity = validated_data.get('assets_quantity', instance.assets_quantity)

        return instance


class RequesterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
    from_location = serializers.CharField(max_length=100)
    to_location = serializers.CharField(max_length=100)
    date_time = serializers.DateTimeField()
    flexible_timing = serializers.BooleanField()
    no_of_assets = serializers.IntegerField()
    asset_type = serializers.ChoiceField(choices=ASSET_TYPE)
    asset_sensitivity = serializers.ChoiceField(choices=ASSET_SENSITIVITY)
    whom_to_deliver = serializers.CharField(max_length=255)
    accepted_person = serializers.CharField(max_length=255)
    status = serializers.ChoiceField(choices=STATUS)

    def create(self, validated_data):
        return Requester(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.from_location = validated_data.get('from_location', instance.from_location)
        instance.to_location = validated_data.get('to_location', instance.to_location)
        instance.date_time = validated_data.get('date_time', instance.date_time)
        instance.flexible_timing = validated_data.get('flexible_timing', instance.flexible_timing)
        instance.no_of_assets = validated_data.get('no_of_assets', instance.no_of_assets)
        instance.asset_type = validated_data.get('asset_type', instance.asset_type)
        instance.asset_sensitivity = validated_data.get('asset_sensitivity', instance.asset_sensitivity)
        instance.whom_to_deliver = validated_data.get('whom_to_deliver', instance.whom_to_deliver)
        instance.accepted_person = validated_data.get('accepted_person', instance.accepted_person)
        instance.status = validated_data.get('status', instance.status)

        return instance
    