from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag right now")
        return redirect(reverse('products'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NxoU1FzBWPulS5S167Ckz6GvMoFCV30i28XbeFR2mZO5mXOYKVrgBauNTIH21SHM5sjj5lSRhwpjiJQuTj2jmHU00mD0xp0A0',
        'client_secret': 'test client secret',
    }
    
    return render(request, template, context)
