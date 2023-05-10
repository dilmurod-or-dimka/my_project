from django.contrib import admin
from .models import Services, Human, ServicesImage, HumanImage, About


# Register your models here.


class ServicesImageInline(admin.TabularInline):
    model = ServicesImage
    extra = 1


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "descr", "slug")
    list_display_links = ("pk", "title")
    preserve_filters = {"slug": ("title",)}
    inlines = [ServicesImageInline]


class HumanImageInline(admin.TabularInline):
    model = HumanImage
    extra = 1


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "descr", "does_work", "slug")
    list_display_links = ("pk", "title")
    preserve_filters = {"slug": ("title",)}
    inlines = [HumanImageInline]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("pk", "descr", "slug")
    list_display_links = ("pk",)
    preserve_filters = {"slug": ("descr",)}
