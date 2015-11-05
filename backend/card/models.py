from django.contrib.auth.models import User
from django.db import models
from profile.models import Profile


# ##################
# ##### MODELS #####
# ##################

class Card(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='Card_created_by')
    is_active = models.BooleanField(default=False)
    question = models.ForeignKey('Question', related_name='Card_question')
    association = models.ForeignKey('Association', related_name='Card_association', null=True, blank=True)

    def __unicode__(self):
        return '%s (%s)' % (self.question.label, self.association.label if self.association else '')


class CardAnswer(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Profile, related_name='CardAnswer_created_by')
    card = models.ForeignKey(Card, related_name='CardAnswer_card')
    answer = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return '%s - %s (%s)' % (self.answer, self.card.question.label, self.card.association.label)


# ####################
# ##### PARTIALS #####
# ####################

class Question(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='Question_created_by')
    is_active = models.BooleanField(default=False)
    label = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.label


class Association(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='Association_created_by')
    is_active = models.BooleanField(default=False)
    label = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.label


# #######################
# ##### SERIALIZERS #####
# #######################

