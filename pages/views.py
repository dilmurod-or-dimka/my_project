from django.shortcuts import render, HttpResponse
from .models import Human, Services, About, Blog
from django.core.paginator import Paginator


# Create your views here.


def home_view(request):
    humans = Human.objects.all()[:3]
    services = Services.objects.all()[:3]
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
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 4)
    page = request.GET.get("page")
    result = paginator.get_page(page)
    context = {
        "blogs": result
    }
    return render(request, "pages/blog.html", context)


def contact_view(request):
    return render(request, "pages/contact.html")




# TODO:
#  создать регестрацию
#  сделать что-то с контактом
#  создать детальную cтраницу для блока
#  создать модельки для блока
#  создать детальную чтраницу для service
#  что-то придумать с Advantegrs в about, и создать модельки для Advantegrs
#  добавить поле для комментария в home
#  Сдлать укоротитель текста дял сервисов