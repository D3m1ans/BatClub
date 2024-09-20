from django.shortcuts import render
from cards.models import Card

# Create your views here.

def index(request):
    object = Card.objects.first()
    data = {
        'title': 'BatClub',
        'object': object,
    }
    return render(request, 'main/index.html', data)