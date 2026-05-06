from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/shop.html', context)

def categories_view(request, slug=None):
    p = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=p).order_by('-published_date')
    context = {'products': products}
    return render(request, 'categories.html', context)

def product_view(request, slug=None):
    product = Product.objects.get(slug=slug)
    return render(request, 'shop/product.html', {'product': product})
