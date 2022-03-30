from django.urls import path
from .views import pokemon_guide, pokemon_guide_detail

urlpatterns = [
    path('', pokemon_guide),
    path('<int:pokemon_id>/', pokemon_guide_detail),
]
