from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.CardListView.as_view()), name='index'),
    path('cards/<int:pk>/', login_required(views.CardDetailView.as_view()), name='cards-detail'),
    path('cards/<int:pk>/delete', login_required(views.CardDeleteView.as_view()), name='cards-delete'),
    path('switch-card-status/<int:pk>/', login_required(views.switch_card_status_view), name='switch-card-status'),
    path('card-generator/', login_required(views.generator_form_view), name='card-generator'),
]
