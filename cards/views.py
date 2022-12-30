from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, DeleteView
from django.shortcuts import redirect, render
from django.contrib import messages
from .filters import CardFilter
from .forms import CardGenForm

from .models import Card
from .services import switch_status, generate_cards


class CardListView(ListView):
    model = Card
    template_name = "cards/index.html"
    context_object_name = 'cards'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CardFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context


class CardDetailView(DetailView):
    model = Card


class CardDeleteView(DeleteView):
    model = Card
    success_url = '/'


def switch_card_status_view(request, **kwargs):
    path_to_return = request.headers['Referer'].replace(f'http://{request.headers["Host"]}', '')
    switched_ok = switch_status(kwargs)
    if not switched_ok:
        messages.warning(request, 'Невозможно активировать карту - истек срок действия')
    return redirect(path_to_return)


def generator_form_view(request):
    form = CardGenForm()

    if request.method == 'POST':
        form = CardGenForm(request.POST)
        if form.is_valid():
            generate_cards(form.cleaned_data)
            messages.success(request, 'Информация о новых картах успешно добавлена в базу данных!')
            return HttpResponseRedirect('/')
        else:
            form = CardGenForm()

    return render(request, 'cards/card_generator_form.html', {'form': form})
