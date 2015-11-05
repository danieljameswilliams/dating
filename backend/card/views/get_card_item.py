import simplejson as json
from django.http import HttpResponse
from card.models import Card


def get_card_item(request, card_id):
    card_set = Card.objects.get(is_active=True, id=card_id)
    card_item = card_set[0] if card_set.count() == 1 else None

    if card_item:
        context = {
            'card': {
                'id': card_item.id,
                'association': card_item.association.label if card_item.association else None,
                'question': card_item.question.label
            }
        }
        return HttpResponse(json.dumps(context))
    else:
        return HttpResponse(status=204)
