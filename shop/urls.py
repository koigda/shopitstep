from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop'),
    path('categories/<slug:slug>', views.categories_view, name='shop_categories'),
    path('products/<slug:slug>', views.product_view, name='shop_products'),
]