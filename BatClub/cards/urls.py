from django.urls import path
from . import views

urlpatterns = [
    path('batman', views.card_batman, name='batman-card'),
    path('<int:pk>', views.HeroDetailView.as_view(), name='hero-detail')
]
