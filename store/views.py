from django.shortcuts import render, get_object_or_404

from .models import Product

from category.models import Category


# Create your views here.


def store(request, category_slug=None):
    category = None
    products = None

    catogories = Category.objects.all()

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        "products_count": product_count,
        "products": products,
        "categories": catogories
    }

    return render(request, "store/store.html", context=context)
