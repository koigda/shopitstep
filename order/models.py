from django.db import models

from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order {self.id}"

    def total_coast(self):
        return sum(item.get_coast() for item in self.items.all())




class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order , on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_coast(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product.name} {self.quantity} {self.price}"

