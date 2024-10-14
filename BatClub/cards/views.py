import re
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Card


# Create your views here.

class HeroDetailView(DetailView):
    model = Card
    template_name = 'cards/hero_detail.html'
    context_object_name = 'card'