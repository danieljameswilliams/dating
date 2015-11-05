import simplejson as json
from django.http import HttpResponse
from card.models import Card
from card.models import CardAnswer
from profile.models import Profile


def get_card_list(request, profile_id):
    # First we find the user who needs the new list of cards
    current_user = Profile.objects.get(id=profile_id)

    # But so he doesn't get cards he already has answered, we need to find
    # the id of those cards, and exclude them from the "card_set"
    card_answer_set = CardAnswer.objects.filter(created_by=current_user)
    card_answer_list = card_answer_set.values('id')
    card_set = Card.objects.filter(is_active=True).exclude(id__in=card_answer_list)
    card_list = list()

    for card_item in card_set:
        card_context = {
            'id': card_item.id,
            'association': card_item.association.label if card_item.association else None,
            'question': card_item.question.label
        }
        card_list.append(card_context)

    if card_set.count() > 0:
        context = {
            'cards': card_list
        }
        return HttpResponse(json.dumps(context))
    else:
        # Telling the client "204: No Content" with an empty response
        return HttpResponse(status=204)
