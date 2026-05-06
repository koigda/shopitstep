from django.contrib.auth.models import User

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=120, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def save(self, *args, **kwargs):
        if not self.slug:
           self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=120, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name = "Загаловок")
    slug = models.SlugField(max_length=220, blank=True)
    content = models.TextField(verbose_name = "Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name = "Дата публікації")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = "Категорії")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Ім'я")
    tags = models.ManyToManyField(Tag, blank=True)
    img = models.URLField(
        default="https://www.shutterstock.com/image-vector/default-ui-image-placeholder-wireframes-600nw-1037719192.jpg")



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Ім'я")
    comment = models.TextField(verbose_name = "Коментарій")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата публікації")

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарії"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)





