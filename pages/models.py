from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Services(models.Model):
    title = models.CharField(verbose_name="Название услуги", max_length=150, unique=True)
    descr = models.TextField(verbose_name="Описание услуги  ")
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    def get_photo_service(self):
        photo = self.servicesimage_set.all().first()
        if photo is not None:
            return photo.photo.url
        return "https://images.satu.kz/126101312_w640_h640_razdel-v-razrabotketovary.jpg"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Услугу"
        verbose_name_plural = "Услуги"


class ServicesImage(models.Model):
    photo = models.ImageField(verbose_name="Фото", upload_to="services/", blank=True, null=True)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)


class Human(models.Model):
    title = models.CharField(verbose_name="Имя человека", max_length=150, unique=True)
    descr = models.TextField(verbose_name="Описание человека")
    does_work = models.BooleanField(verbose_name="Работает?", default=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    def get_photo_human(self):
        photo = self.humanimage_set.all().first()
        if photo is not None:
            return photo.photo.url
        return "https://images.satu.kz/126101312_w640_h640_razdel-v-razrabotketovary.jpg"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"


class HumanImage(models.Model):
    photo = models.ImageField(verbose_name="Фото", upload_to="humans/", blank=True, null=True)
    humans = models.ForeignKey(Human, on_delete=models.CASCADE)
