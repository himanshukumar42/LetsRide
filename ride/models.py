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

)


class Rider(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    _from = models.CharField(max_length=100)
    _to = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    flexible_timing = models.BooleanField()
    travel_medium = models.CharField(max_length=255, choices=TRAVEL_MEDIUM, default=TRAVEL_MEDIUM.Car)
    assets_quantity = models.IntegerField()


class Requester(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    _from = models.CharField(max_length=100)
    _to = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    flexible_timing = models.BooleanField()
    no_of_assets = models.IntegerField()
    asset_type = models.CharField(max_length=150, choices=ASSET_TYPE, default=ASSET_TYPE.Laptop)
    asset_sensitivity = models.CharField(max_length=150, choices=ASSET_SENSITIVITY, default=ASSET_SENSITIVITY.Normal)
    whom_to_deliver = models.CharField(max_length=255)
    accepted_person = models.CharField(max_length=255)
    status = models.
