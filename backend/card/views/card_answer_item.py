import simplejson as json
from django.http import HttpResponse, HttpResponseForbidden
from card.models import CardAnswer
from profile.models import Profile


def get_card_answer_item(request, card_answer_id, profile_id):
    # TODO: Add a the actual current_user
    # First we find the user who needs the new list of cards
    current_user = Profile.objects.get(id=profile_id)

    # But so he doesn't get cards he already has answered, we need to find
    # the id of those cards, and exclude them from the "card_set"
    card_answer_set = CardAnswer.objects.filter(id=card_answer_id)
    card_answer_item = card_answer_set[0] if card_answer_set.count() == 1 else None

    if card_answer_item and card_answer_item.created_by is current_user:
        context = {
            'card_answer': {
                'id': card_answer_item.id,
                'created_at': card_answer_item.created_on,
                'answer': card_answer_item.answer,
                'card': {
                    'id': card_answer_item.card.id,
                    'association': card_answer_item.card.association.label if card_answer_item.card.association else None,
                    'question': card_answer_item.card.question.label
                }
            }
        }
        return HttpResponse(json.dumps(context))
    elif card_answer_item and card_answer_item.created_by is not current_user:
        return HttpResponseForbidden()
    else:
        return HttpResponse(status=204)
