from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    """ A View to show the products and include sorting and searcg queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A View to show individual product information  """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
