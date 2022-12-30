from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

alphanumeric = RegexValidator(r'^[0-9A-Z]*$', 'Only upper case letters and numbers are allowed.')
numeric = RegexValidator(r'^[0-9]*$', 'Only numbers are allowed.')


class Card(models.Model):
    series = models.CharField(max_length=4, validators=[alphanumeric])
    number = models.CharField(max_length=8, blank=True, unique=True, validators=[numeric])
    date_released = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField()
    status = models.BooleanField(default=False)

    @property
    def is_expired(self):
        return timezone.now() >= self.date_expiration

    @property
    def is_active(self):
        return self.status and not self.is_expired

    def __str__(self):
        return f'{self.series} {self.number}'

    @property
    def get_payments(self):
        return self.payment_set.all()


class Payment(models.Model):
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    card = models.ForeignKey(to=Card, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.card} - {self.payment_date}'
