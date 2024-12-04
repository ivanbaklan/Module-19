from django.contrib import admin
from django.urls import path

from UrbanDjango.views import index_view
from task1.views import sign_up_by_django, platform_view, game_view, cart_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view),
    path("sign_up_by_django/", sign_up_by_django),
    path("platform/", platform_view),
    path("platform/games/", game_view),
    path("platform/cart/", cart_view),
]
