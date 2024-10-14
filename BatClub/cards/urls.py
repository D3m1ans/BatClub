from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.HeroDetailView.as_view(), name='hero-detail'),
]
