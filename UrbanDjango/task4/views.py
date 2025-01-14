from django.views.generic import TemplateView
from django.shortcuts import render


def platform(request):
    return render(request, "fourth_task/platform.html")


def games(request):
    """
    games = {
        "first": "Atomic Heart",
        "second": "Cyberpank",
        "third": "PayDay 2"
    }
    """
    games = {'games': ['Atomic Heart', 'Cyberpunk 2077','PayDay 2']}

    return render(request, "fourth_task/games.html", context=games)


def cart(request):
    return render(request, "fourth_task/cart.html")

