from decimal import Decimal
from itertools import product

from django.conf import settings
from django.utils.timezone import override

from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product.quantity = str(quantity)
        if product.quantity not in self.cart:
            self.cart[product.quantity] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product.quantity]['quantity'] = quantity
        else:
            self.cart[product.quantity]['quantity'] += quantity

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['quantity'] = product

        for item in cart:
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


