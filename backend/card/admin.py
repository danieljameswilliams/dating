from django.contrib import admin
from card.models import Card, CardAnswer, Question, Association


# ####################
# ##### Register #####
# ####################

admin.site.register(Card)
admin.site.register(CardAnswer)
admin.site.register(Question)
admin.site.register(Association)
