from django.shortcuts import render
from cards.models import Card

# Create your views here.

def index(request):
    objects = Card.objects.all()
    data = {
        'title': 'BatClub',
        'objects': objects,
    }
    return render(request, 'main/index.html', data)