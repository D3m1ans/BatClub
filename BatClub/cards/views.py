import re
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Card


# Create your views here.

class HeroDetailView(DetailView):
    model = Card
    template_name = 'cards/hero_detail.html'
    context_object_name = 'card'

def card_batman(request):
    card = get_object_or_404(Card, id=2)

    appearance = card.appearance
    parts = appearance.split(f'{card.alterego}:')
    hero_part = parts[0].strip()
    person_part = parts[1].strip()

    skills_text = card.skills
    skills = re.split(r'\n\*', skills_text)
    skills = [skill.strip() for skill in skills if skill.strip()]

    allies_text = card.allies
    allies = re.split(r'\n\*', allies_text)
    allies = [allie.strip() for allie in allies if allie.strip()]

    enemies_text = card.enemies
    enemies = re.split(r'\n\*', enemies_text)
    enemies = [enemy.strip() for enemy in enemies if enemy.strip()]

    context = {
        'card': card,
        'hero_part': hero_part,
        'person_part': person_part,
        'skills': skills,
        'allies': allies,
        'enemies': enemies,
    }

    return render(request, 'cards/card_batman.html', context)
