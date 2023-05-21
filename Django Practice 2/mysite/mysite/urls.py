"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import shop.views as shop_views


urlpatterns = [
    path("", shop_views.index, name="index"),
    path("register/", shop_views.register, name="register"),
    path("login/", shop_views.login, name="login"),
    path("info/<id>", shop_views.info, name="info"),
    path("addtocart/<id>", shop_views.addtocart, name="addtocart"),
    path("cart/", shop_views.cart, name="cart"),
    path("search/<q>", shop_views.search, name="search"),
    path("logout", shop_views.logout, name="logout"),
    path("deletecartitem/<id>", shop_views.delete_cart_item, name="deletecartitem"),
    path("admin/", admin.site.urls),
]
