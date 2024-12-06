from django.shortcuts import render
from django.views.generic import ListView

from .forms import UserRegister
from .models import Buyer, Game, Test


class GameListView(ListView):
    model = Game
    template_name = "task1/game_list.html"
    context_object_name = "games"

    def get_paginate_by(self, queryset):
        paginate_by = self.request.GET.get("paginate_by", 1)
        return int(paginate_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["paginate_by"] = self.get_paginate_by(self.get_queryset())
        return context


def validate_vals(username, password, repeat_password, age, info, users):
    try:
        age = int(age)
    except ValueError:
        info["error"] = "возраст должно быть числом"
        return info
    if username in (user.name for user in users):
        info["error"] = "Пользователь уже существует"
        return info
    if password != repeat_password:
        info["error"] = "Пароли не совпадают"
        return info
    if int(age) < 18:
        info["error"] = "Вы должны быть старше 18"
        return info
    info["content"] = f"Приветствуем, {username}!"
    return info


def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if not request.method == "POST":
        info["form"] = UserRegister()
        return render(request, "task1/registration_page.html", context=info)
    form = UserRegister(request.POST)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        repeat_password = form.cleaned_data["repeat_password"]
        age = form.cleaned_data["age"]
        info = validate_vals(username, password, repeat_password, age, info, users)
        if "error" not in info.keys():
            Buyer.objects.create(name=username, balance=0, age=age)
        info["form"] = form
        return render(request, "task1/registration_page.html", context=info)
    else:
        info["error"] = "Ошибка валидации формы"
        return render(request, "task1/registration_page.html", context=info)


def platform_view(request):
    return render(request, "task1/platform.html")


def game_view(request):
    games = Game.objects.all()
    return render(
        request,
        "task1/games.html",
        context={"games": games},
    )


def cart_view(request):
    return render(request, "task1/cart.html")


def fitst_query_set():
    first_buyer = Buyer.objects.create(name="user1", balance=1500.05, age=24)
    second_buyer = Buyer.objects.create(name="user2", balance=42.15, age=52)
    third_buyer = Buyer.objects.create(name="user3", balance=0.05, age=16)

    game1 = Game.objects.create(
        title="Cyber punk 2077",
        cost=31,
        size=46.2,
        description="Game of the year.",
        age_limited=True,
    )
    game2 = Game.objects.create(
        title="Mario",
        cost=5,
        size=0.5,
        description="Old Game.",
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


def admin_task():
    game4 = Game.objects.create(
        title="Test",
        cost=12,
        size=36.6,
        description="-",
        age_limited=True,
    )

    game4.title = "Change title"
    game4.save()
    all_game = Game.objects.all()
    print(all_game)
    game4.delete()
    all_game = Game.objects.all()
    print(all_game)
    filtered = list(Game.objects.filter(age_limited=True))
    print(filtered)


def postgres_task():
    test_obj_1 = Test.objects.create(
        name="Test_1",
    )
    test_obj_2 = Test.objects.create(
        name="Test_2",
    )
    test_obj_3 = Test.objects.create(
        name="Test_3",
    )
    test_obj_1.name = "Change name"
    test_obj_1.save()
    all_test_obj = Test.objects.all()
    print(all_test_obj)
    get_object = Test.objects.get(id=test_obj_1.id)
    print(get_object)
    test_obj_1.delete()
    all_test_obj = Test.objects.all()
    print(all_test_obj)
    filtered = list(Test.objects.filter(id=2))
    print(filtered)
    count = Test.objects.filter(id__gte=1).count()
    print(count)
