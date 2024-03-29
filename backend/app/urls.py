from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # API URLs
    url(r'^api/cards/(?P<profile_id>[0-9]+)/', 'card.views.card_list'),
    url(r'^api/card/(?P<card_id>[0-9]+)/', 'card.views.card_item'),

    url(r'^api/card-answers/(?P<profile_id>[0-9]+)/', 'card.views.card_answer_list'),
    url(r'^api/card-answer/(?P<card_answer_id>\d+)/(?P<profile_id>\d+)/', 'card.views.card_answer_item'),

    # Admin URLs
    url(r'^admin/', include(admin.site.urls)),
]
