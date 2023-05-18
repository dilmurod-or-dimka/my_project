from django.shortcuts import render, HttpResponse
from .models import Human, Services, About, Blog, Comment
from .forms import CommentForm
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


def blog_detail_view(request, slug):
    blog = Blog.objects.get(slug=slug)
    comments = blog.comments.filter(blog=blog)

    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.blog = blog
            form.save()
            return render("blog_detail", blog.slug)

    else:
        form = CommentForm()

    context = {
        "blog": blog,
        "form": form,
        "comments": comments,
    }
    return render(request, "pages/blog_detail.html", context)


# TODO:
#  создать детальную cтраницу для блока
#  создать регестрацию
#  сделать что-то с контактом

# Сделано:
#  создать модельки для блока
#  Сдлать укоротитель текста для сервисов
