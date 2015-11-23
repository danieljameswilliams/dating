import simplejson as json
from django.http import HttpResponse, HttpResponseForbidden
from card.models import CardAnswer, Card
from profile.models import Profile


def get_card_answer_item(request, card_id, profile_id):
    token = request.POST.get('token')

    # First we find the user who needs the new list of cards
    current_user = Profile.objects.get(id=profile_id)

    # But so he doesn't get cards he already has answered, we need to find
    # the id of those cards, and exclude them from the "card_set"
    card_answer_set = CardAnswer.objects.filter(card__id=card_id, created_by=current_user)
    card_answer_item = card_answer_set[0] if card_answer_set.count() == 1 else None

    if card_answer_item:
        context = {
            'card_answer': {
                'id': card_answer_item.id,
                'created_at': card_answer_item.created_on.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'answer': card_answer_item.answer,
                'card': {
                    'id': card_answer_item.card.id,
                    'association': card_answer_item.card.association.label if card_answer_item.card.association else None,
                    'question': card_answer_item.card.question.label
                }
            }
        }

    # ##################
    # ### PUBLIC API ###
    # ##################

    if card_answer_item and current_user.token == token:
        response = HttpResponse(json.dumps(context))
        response['Access-Control-Allow-Origin'] = '*'
        return response
    elif card_answer_item and current_user.token != token:
        response = HttpResponseForbidden()
        response['Access-Control-Allow-Origin'] = '*'
        return response
    else:
        # Telling the client "204: No Content" with an empty response
        response = HttpResponse(status=204)
        response['Access-Control-Allow-Origin'] = '*'
        return response


def post_card_answer_item(request, card_id, profile_id):
    token = request.POST.get('token')

    if card_id and profile_id:
        # First we find the user who needs the new list of cards
        current_user = Profile.objects.get(id=profile_id)

        if current_user.token == token:
            # If the card_answer already exist, we override it's properties.
            # And if it's new, we create it.
            card_item = Card.objects.get(id=card_id)
            card_answer_item, created = CardAnswer.objects.get_or_create(card=card_item, created_by=current_user)
            card_answer_item.answer = request.POST.get('answer').strip()

            if len(card_answer_item.answer) > 0:
                card_answer_item.save()

    # ##################
    # ### PUBLIC API ###
    # ##################

    if not card_id or not profile_id and len(card_answer_item['answer']) > 0:
        # Telling the client "400: Bad Request" with an empty response
        response = HttpResponse(status=400)
        response['Access-Control-Allow-Origin'] = '*'
        return response
    elif card_answer_item and current_user.token == token:
        response = HttpResponse(status=200)
        response['Access-Control-Allow-Origin'] = '*'
        return response
    elif card_answer_item and current_user.token != token:
        response = HttpResponseForbidden()
        response['Access-Control-Allow-Origin'] = '*'
        return response
    else:
        # Telling the client "204: No Content" with an empty response
        response = HttpResponse(status=204)
        response['Access-Control-Allow-Origin'] = '*'
        return response
