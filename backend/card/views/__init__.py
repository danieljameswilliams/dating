from django.http import HttpResponse
from card.views.card_list import get_card_list
from card.views.card_item import get_card_item
from card.views.card_answer_list import get_card_answer_list
from card.views.card_answer_item import get_card_answer_item


# ################
# ##### CARD #####
# ################

def card_list(request):
    if request.method == 'GET':
        return get_card_list(request)
    elif request.method == 'PUT':
        # Status: Not Implemented
        return HttpResponse(status=501)


def card_item(request):
    if request.method == 'GET':
        return get_card_item(request)
    elif request.method == 'PUT':
        # Status: Not Implemented
        return HttpResponse(status=501)


# #######################
# ##### CARD ANSWER #####
# #######################

def card_answer_list(request):
    if request.method == 'GET':
        return get_card_answer_list(request)
    elif request.method == 'PUT':
        # Status: Not Implemented
        return HttpResponse(status=501)


def card_answer_item(request):
    if request.method == 'GET':
        return get_card_answer_item(request)
    elif request.method == 'PUT':
        # Status: Not Implemented
        return HttpResponse(status=501)
