from django.shortcuts import render, HttpResponse
from .models import Human, Services

# Create your views here.


def home_view(request):
    humans = Human.objects.all()
    services = Services.objects.all()
    context = {
        "services": services,
        "humans": humans
    }
    return render(request, "pages/index.html", context)


def about_view(request):
    return render(request, "pages/about.html")
