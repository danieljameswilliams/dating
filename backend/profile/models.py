from django.contrib.auth.models import User
from django.db import models


# #################
# ##### MODEL #####
# #################

class Profile(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='Profile_user')
    name = models.CharField(max_length=200)
    location = models.ForeignKey('Location', related_name='Profile_location')

    def __unicode__(self):
        return self.name


# ####################
# ##### PARTIALS #####
# ####################

class Location(models.Model):
    address = models.CharField(max_length=200, null=True)
    zip = models.CharField(max_length=15, null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    latitude = models.CharField(max_length=50, null=True)
    longitude = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.address
