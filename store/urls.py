"""eshop URL Configuration

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
from django.urls import path, re_path
from .views import index, login, sign, cart, checkout, orders, forgotpass, otp, ordermanage, profile, main, products

urlpatterns = [
    path("index", index.Index.as_view()  , name="index"),
    path("", main.Main.as_view()  , name="main"),
    path("signup", sign.Signup.as_view() , name="signup"),
    path("login", login.Login.as_view() , name="login"),
    path("logout", login.logout, name="logout"),
    path("cart", cart.Cart.as_view(), name="cart"),
    path("check-out", checkout.CheckOut.as_view(), name="checkout"),
    path("orders", orders.OrderView.as_view(), name="orders"),
    path("forgotpass", forgotpass.Forgotpass.as_view(), name="forgotpass"),
    path("otp", otp.Otp.as_view(), name="otp"),
    path("ordermanage", ordermanage.Ordermanage.as_view(), name="ordermanage"),
    path("profile", profile.Profile.as_view(), name="profile"),
    path("products", products.Products.as_view(), name="products"),
]
