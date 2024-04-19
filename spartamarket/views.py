from django.shortcuts import render
from products.models import Products

def index(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'index.html', context)