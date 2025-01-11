from django.views.generic import TemplateView
from django.shortcuts import render


def platform(request):
    return render(request, "third_task/platform.html")


def games(request):
    games = {
        "first": "Atomic Heart",
        "second": "Cyberpank",
        "third": "PayDay 2"

    }
    return render(request, "third_task/games.html", context=games)


def cart(request):
    return render(request, "third_task/cart.html")

