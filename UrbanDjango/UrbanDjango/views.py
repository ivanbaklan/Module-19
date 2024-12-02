from django.shortcuts import render


def index_view(request):
    return render(request, "UrbanDjango/index_template.html")
