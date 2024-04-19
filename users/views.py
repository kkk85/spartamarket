from django.shortcuts import render,get_object_or_404, redirect
from accounts.models import User
from products.models import Products
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required



# profile
@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    UserProducts = user.products_user.all()
    Userlikes = user.like_products.all()
    Userfollows = user.follwers.all()
    context = {'user': user, 'UserProducts': UserProducts, 'Userlikes':Userlikes,'Userfollows':Userfollows }
    return render(request, 'users/profile.html', context)


@login_required
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Products, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect('index')
    return redirect('accounts:login')

@login_required
def follow(request, pk):
    if request.user.is_authenticated:
        menber = get_object_or_404(get_user_model(), pk=pk)
        if menber != request.user:
            if menber.follwers.filter(pk=request.user.pk).exists():
                menber.follwers.remove(request.user)
            else:
                menber.follwers.add(request.user)
        return redirect('users:profile', menber.pk)
    return redirect('account:login')