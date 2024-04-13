from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import AddToCartForm
from .models import Product, CartItem

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'WebsiteApp/products.html', {'products': products})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

from .models import CartItem, Product

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)

    if product and request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    return redirect('home')

def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect('cart')

def multiply(value, arg):
    return value * arg

def checkout_view(request):
    return render(request, 'checkout.html')

def remove_from_cart(request, item_id):
    CartItem.objects.filter(id=item_id).delete()
    return redirect('cart')