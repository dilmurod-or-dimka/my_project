from django.shortcuts import render, HttpResponse
from .models import Human, Services, About


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
    humans = Human.objects.all()
    abouts = About.objects.all()
    context = {
        "abouts": abouts,
        "humans": humans
    }
    return render(request, "pages/about.html", context)


def service_view(request):
    services = Services.objects.all()
    context = {
        "services": services,
    }
    return render(request, "pages/services.html", context)


def blog_view(request):
    return render(request, "pages/blog.html")


def contact_view(request):
    return render(request, "pages/contact.html")
