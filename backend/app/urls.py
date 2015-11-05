from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # API URLs
    url(r'^api/cards/', 'card.views.get_card_list'),
    url(r'^api/cards/(?P<card_id>[0-9]+)/', 'card.views.get_card_item'),

    url(r'^api/card-answers/(?P<profile_id>[0-9]+)/', 'card.views.get_card_answer_list'),
    url(r'^api/card-answers/(?P<card_answer_id>[0-9]+)/(?P<profile_id>[0-9]+)/', 'card.views.get_card_answer_item'),

    # Admin URLs
    url(r'^admin/', include(admin.site.urls)),
]
