from django.shortcuts import render, get_object_or_404
from .models import Card


# Create your views here.

def card_batman(request):
    card = get_object_or_404(Card, id=2)
    return render(request, 'cards/card_batman.html', {'card': card})