from django import forms


class CardGenForm(forms.Form):
    validity_opts = (
        ('Месяц', 'Месяц'),
        ('Полгода', 'Полгода'),
        ('Год', 'Год'),
    )
    series = forms.CharField(label='Серия', max_length=4)
    amount = forms.IntegerField(label='Количество', max_value=50)
    validity = forms.ChoiceField(label='Срок действия', choices=validity_opts)
