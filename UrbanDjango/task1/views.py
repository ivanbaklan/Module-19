from django.shortcuts import render
from .models import Buyer, Game


def fitst_query_set():
    first_buyer = Buyer.objects.create(name="user1", balance=1500.05, age=24)
    second_buyer = Buyer.objects.create(name="user2", balance=42.15, age=52)
    third_buyer = Buyer.objects.create(name="user3", balance=0.05, age=16)

    game1 = Game.objects.create(
        title="Cyber punk 2077",
        cost=31,
        size=46.2,
        description="How kills Mark?",
        age_limited=True,
    )
    game2 = Game.objects.create(
        title="Mario",
        cost=5,
        size=0.5,
        description="How kills Mark?",
        age_limited=False,
    )
    game3 = Game.objects.create(
        title="Hitman",
        cost=12,
        size=36.6,
        description="How kills Mark?",
        age_limited=True,
    )
    Game.objects.get(id=game1.id).buyer.set((first_buyer, second_buyer))
    Game.objects.get(id=game2.id).buyer.set((first_buyer, second_buyer, third_buyer))
    Game.objects.get(id=game3.id).buyer.set((first_buyer,))
