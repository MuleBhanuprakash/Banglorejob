from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.gis import geos
from geopy.geocoders import GoogleV3


# Create your models here.


class Address(models.Model):
    Name = models.CharField(max_length=30)
    Job = models.CharField(max_length=30)
    Address1 = models.CharField(max_length=30)
    Address2 = models.CharField(max_length=30)
    Area = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
    Pinode = models.CharField(max_length=30)
    location = models.PointField(u"longitude/latitude", blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.Name

    def __unicode__(self):
        return self.id

    def save(self, **kwargs):
        if not self.location:
            address = u'%s %s %s %s %s %s %s' % (self.Address1, self.Address2,
                                                 self.Area, self.City,
                                                 self.State, self.Pincode, self.Country)
            address = address.encode('utf-8')
            geocoder = GoogleV3(api_key='my API key')
            try:
                _, latlon = geocoder.geocode('address')

            except ValueError:

                pass
            else:
                point = "POINT(%s %s)" % (latlon[1], latlon[0])
                self.location = geos.fromstr(point)
        super(Address, self).save()
