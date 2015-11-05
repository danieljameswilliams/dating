from django.db import models
from card.models import Card
from profile.models import Profile


# #################
# ##### MODEL #####
# #################

class Match(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    profile1 = models.ForeignKey(Profile, related_name='Match_profile1')
    profile2 = models.ForeignKey(Profile, related_name='Match_profile2')
    card = models.ForeignKey(Card, related_name='Match_card')
    matches = models.ManyToManyField('MatchItem', related_name='Match_matches')


# ####################
# ##### PARTIALS #####
# ####################

class MatchItem(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    card_profile1 = models.ForeignKey(Card, related_name='MatchItem_card_profile1')
    card_profile2 = models.ForeignKey(Card, related_name='MatchItem_card_profile2')
