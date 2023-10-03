from django.shortcuts import render

def view_bag(request):
    """ A View to return the bag page """
    return render(request, 'bag/bag.html')
