from django.contrib import admin
from profile.models import Profile, Location


# ####################
# ##### Register #####
# ####################

admin.site.register(Profile)
admin.site.register(Location)
