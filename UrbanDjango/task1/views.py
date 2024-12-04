from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game


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
