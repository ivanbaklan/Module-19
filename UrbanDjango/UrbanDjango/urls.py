from django.contrib import admin
from django.urls import path

from task1.views import (GameListView, cart_view, game_view, platform_view,
                         sign_up_by_django)
from UrbanDjango.views import index_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view),
    path("sign_up_by_django/", sign_up_by_django),
    path("platform/", platform_view),
    path("platform/games/", game_view),
    path("platform/cart/", cart_view),
    path("platform/games_list/", GameListView.as_view(), name="game_list"),
]
