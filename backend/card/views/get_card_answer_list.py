import simplejson as json
from django.http import HttpResponse
from card.models import CardAnswer
from profile.models import Profile


def get_card_answer_list(request, profile_id):
    # TODO: Add a the actual current_user
    # First we find the user who needs the new list of cards
    current_user = Profile.objects.get(id=profile_id)

    # But so he doesn't get cards he already has answered, we need to find
    # the id of those cards, and exclude them from the "card_set"
    card_answer_set = CardAnswer.objects.filter(created_by=current_user)
    card_answer_list = list()

    for card_answer_item in card_answer_set:
        card_answer_context = {
            'id': card_answer_item.id,
            'created_at': card_answer_item.created_on,
            'answer': card_answer_item.answer,
            'card': {
                'id': card_answer_item.card.id,
                'association': card_answer_item.card.association.label if card_answer_item.card.association else None,
                'question': card_answer_item.card.question.label
            }
        }
        card_answer_list.append(card_answer_context)

    if card_answer_set.count() > 0:
        context = {
            'card_answers': card_answer_list
        }
        return HttpResponse(json.dumps(context))
    else:
        # Telling the client "204: No Content" with an empty response
        return HttpResponse(status=204)
