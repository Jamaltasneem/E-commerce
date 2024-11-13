from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from .forms import OrderForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

from django.contrib.auth.decorators import login_required
def index(request):
    products=Product.objects.all()
    return render(request, 'index.html', {'products': products})
    

def new(request):
    return HttpResponse('hello there')    


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'products/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'products/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.product = product
            order.save()
            messages.success(request, 'Order placed successfully!')
            return render(request, 'products/order_confirmation.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'products/place_order.html', {'form': form, 'product': product})