import django_filters

from .models import Card


class CardFilter(django_filters.FilterSet):
    date_released = django_filters.IsoDateTimeFromToRangeFilter()
    date_expiration = django_filters.IsoDateTimeFromToRangeFilter()

    class Meta:
        model = Card
        fields = {
            'series': ['exact'],
            'number': ['icontains'],
            'status': ['exact'],
        }
