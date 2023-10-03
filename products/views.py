from django.shortcuts import render
from .models import Product

def all_products(request):
    """ A View to show the products and include sorting and searcg queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
