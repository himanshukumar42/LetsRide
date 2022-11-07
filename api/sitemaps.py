from django.contrib.sitemaps import Sitemap
from ride.models import Rider, Requester


class RiderSiteMap(Sitemap):
    change_freq = "daily"
    priority = 0.7

    def items(self):
        return Rider.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class RequesterSiteMap(Sitemap):
    change_freq = "daily"
    priority = 0.7

    def items(self):
        return Requester.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
