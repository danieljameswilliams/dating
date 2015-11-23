from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from card.views.card_list import get_card_list
from card.views.card_item import get_card_item
from card.views.card_answer_list import get_card_answer_list
from card.views.card_answer_item import get_card_answer_item
from card.views.card_answer_item import post_card_answer_item


# ################
# ##### CARD #####
# ################

@csrf_exempt
def card_list(request, profile_id):
    if request.method == 'GET':
        return get_card_list(request, profile_id)
    elif request.method == 'POST':
        # Status: Not Implemented
        return HttpResponse(status=501)

@csrf_exempt
def card_item(request, card_id):
    if request.method == 'GET':
        return get_card_item(request, card_id)
    elif request.method == 'POST':
        # Status: Not Implemented
        return HttpResponse(status=501)


# #######################
# ##### CARD ANSWER #####
# #######################

@csrf_exempt
def card_answer_list(request, profile_id):
    if request.method == 'GET':
        return get_card_answer_list(request, profile_id)
    elif request.method == 'POST':
        # Status: Not Implemented
        return HttpResponse(status=501)


@csrf_exempt
def card_answer_item(request, card_answer_id, profile_id):
    print('Entering card_answer_item')
    if request.method == 'GET':
        return get_card_answer_item(request, card_answer_id, profile_id)
    elif request.method == 'POST':
        return post_card_answer_item(request, card_answer_id, profile_id)
