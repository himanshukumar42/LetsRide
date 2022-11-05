from django.contrib.auth.models import User
from django.utils import timezone
from model_utils import Choices
from django.db import models

# Create your models here.


TRAVEL_MEDIUM = Choices(
    ('Car', 'car'),
    ('Bus', 'bus'),
    ('Train', 'train'),
)

ASSET_TYPE = Choices(
    ('Laptop', 'laptop'),
    ('Travel_Bag', 'travel_bag'),
    ('Package', 'package')

)

ASSET_SENSITIVITY = Choices(
    ('Highly_Sensitive', 'highly_sensitive'),
    ('Sensitive', 'sensitive'),
    ('Normal', 'normal')
)

STATUS = Choices(
    ('Confirm', 'confirm'),
    ('Pending', 'pending'),
    ('Expired', 'expired')
)


class Rider(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255)
    from_location = models.CharField(max_length=150, null=False)
    to_location = models.CharField(max_length=150, null=False)
    date_time = models.DateTimeField(null=False)
    flexible_timing = models.BooleanField(default=False, null=False)
    travel_medium = models.CharField(max_length=255, choices=TRAVEL_MEDIUM, default=TRAVEL_MEDIUM.Car, null=True)
    assets_quantity = models.IntegerField(default=0, null=False)
    created_at = models.DateTimeField(editable=False, default=timezone.now(), null=False)
    updated_at = models.DateTimeField(editable=True, default=timezone.now(), null=False)
    deleted_at = models.DateTimeField(editable=False, null=True)
    row_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_time']


class Requester(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=255, null=True)
    from_location = models.CharField(max_length=100, null=False)
    to_location = models.CharField(max_length=100, null=False)
    date_time = models.DateTimeField()
    flexible_timing = models.BooleanField(default=False)
    no_of_assets = models.IntegerField(default=1)
    asset_type = models.CharField(max_length=150, choices=ASSET_TYPE, default=ASSET_TYPE.Laptop)
    asset_sensitivity = models.CharField(max_length=150, choices=ASSET_SENSITIVITY, default=ASSET_SENSITIVITY.Normal)
    whom_to_deliver = models.CharField(max_length=255, null=True)
    accepted_person = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=150, choices=STATUS, default=STATUS.Confirm)
    created_at = models.DateTimeField(editable=False, default=timezone.now(), null=False)
    updated_at = models.DateTimeField(editable=True, default=timezone.now(), null=False)
    deleted_at = models.DateTimeField(editable=False, null=True)
    row_deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['date_time']

