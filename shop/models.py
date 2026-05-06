import os

from PIL import Image
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shop/products')
    thumbnail = models.ImageField(upload_to='shop/products/thumbnail', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.thumbnail:
            self.create_thumbnail()

    def create_thumbnail(self):
        img_path = self.image.path
        thumb_path = os.path.join(os.path.dirname(img_path), "categories", os.path.basename(img_path))
        os.path.basename(img_path)
        img = Image.open(img_path)
        img.thumbnail((200, 200))
        os.makedirs(os.path.dirname(thumb_path), exist_ok=True)
        img.save(thumb_path)
        self.thumbnail = f"shop/products/thumbnail{os.path.basename(img_path)}"
        super().save(update_fields=["thumbnail"])

def __str__(self):
    return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shop/products')
    thumbnail = models.ImageField(upload_to='shop/products/thumbnail', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.TextField()

class ProductImeges(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop/products/')