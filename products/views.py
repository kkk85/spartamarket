from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormProducts
from .models import Products
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_http_methods

# Create your views here.
def product(request,pk):
    products = get_object_or_404(Products,pk=pk)
    context = {'products': products}
    return render(request, 'products/templates.users/products.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = FormProducts(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('index')
    else:
            form = FormProducts()
    context = { "form":form}
    return render(request, 'products/templates.users/create.html', context)

@login_required
def update(request, pk):
    product = get_object_or_404(Products,pk=pk)
    if request.method == 'POST':
        form = FormProducts(request.POST, request.FILES,instance=product )
        if form.is_valid():
            form.save()
            return redirect('products:product',pk)
    else:
        form = FormProducts(instance=product)
    context = {'form':form, 'product':product}
    return render(request, 'products/templates.users/update.html', context)

@login_required
def delete(request, pk):
    deletes = get_object_or_404(Products,pk=pk)
    Products.delete(deletes)
    return redirect('index')
