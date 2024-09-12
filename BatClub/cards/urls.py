from django.urls import path
from . import views

urlpatterns = [
    path('batman', views.card_batman, name='batman-card'),
    path('nightwing', views.card_nightwing, name='nightwing-card'),
]
