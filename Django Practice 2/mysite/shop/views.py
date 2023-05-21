from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, CartItem
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.db.models import Q
# Create your views here.
def index(request):
    context = {
        "products": Product.objects.all(),
    }
    if request.method == 'POST':
         q = request.POST['search']
         return redirect(f'/search/{q}')
    return render(request, "shop/index.html", context=context)

def search(request, q):
     products = Product.objects.filter(Q(name__contains=q))
     context = {
          "products": products,
          'q': q,
     }
     return render(request, "shop/search.html", context=context)

def register(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            new_user = User(username=username, password=password)
            new_user.save()
        except IntegrityError:
            messages.error(request,"Username is aldready taken, please try again")
        
    return render(request, "shop/register.html")

def login(request):
    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                    auth_login(request, user)
                    messages.success(request, f"Logged in successfully as {username}")
                    return redirect("index")
            else:
                messages.error(request, f"Username or password invalid. Please try again")
        
    return render(request, "shop/login.html")

def info(request, id):
     product = Product.objects.filter(id=id).first()

     context = {'product': product}

     return render(request, "shop/info.html", context=context)


def addtocart(request, id):
     if request.user.is_authenticated:
          
        product = Product.objects.filter(id=id).first()


        new_cart_item = CartItem(name=product.name, description=product.description, price=product.price, user=request.user)
        new_cart_item.save()
        messages.success(request, f"{product.name} Added to cart!")
        return redirect('index')  

     else:
          messages.error(request, f"You need to be logged in to add items to the cart!")
          return redirect("info", id=id)

def logout(request):
     auth_logout(request)
     messages.success(request, "Logged out successfully")
     return redirect('index')

def cart(request):
     if request.user.is_authenticated:
          
        cart_items = CartItem.objects.filter(user=request.user).all()
        tot = 0
        for cart_item in cart_items:
             tot += cart_item.price
        context = {
             'cart_items': cart_items,
             'total': tot,
             'amt': len(cart_items),
        }
        return render(request, "shop/cart.html", context=context)

     else:
          messages.error(request, f"You need to be logged to view your cart")
          return redirect('index') 

def delete_cart_item(request, id): 
     if request.user.is_authenticated:
          cart_item = CartItem.objects.filter(user=request.user, id=id).first()
          cart_item.delete()
          return redirect('cart')
     else:
          return redirect('index')
    