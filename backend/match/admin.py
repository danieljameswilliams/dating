from django.contrib import admin
from match.models import Match, MatchItem


# ####################
# ##### Register #####
# ####################

admin.site.register(Match)
admin.site.register(MatchItem)
