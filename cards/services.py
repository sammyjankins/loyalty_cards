from django.utils import timezone

from dateutil.relativedelta import relativedelta

from .models import Card
from random import randrange


def switch_status(kwargs):
    card = Card.objects.get(pk=kwargs['pk'])
    if not card.is_expired:
        card.status = not card.status
        card.save()
        return True
    elif card.status:
        card.status = False
        card.save()
    return False


def generate_cards(kwargs):
    months_delta = {
        'Месяц': 1,
        'Полгода': 6,
        'Год': 12,
    }
    fresh_numbers = [number for _ in range(int(kwargs['amount']))
                     if (number := str(randrange(0, 99999999)).zfill(8))
                     if not Card.objects.filter(number=number).exists()]
    date_expiration = timezone.now() + relativedelta(months=months_delta[kwargs['validity']])
    for number in fresh_numbers:
        Card.objects.create(series=kwargs['series'], number=number, date_expiration=date_expiration)
