from django.test import TestCase
from ride.models import Rider


class RiderTestCase(TestCase):
    def setUp(self) -> None:
        Rider.objects.create(name="test", description="This is test")
