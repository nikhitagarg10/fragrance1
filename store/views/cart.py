from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product

class Cart(View):
    def get(self, request):
        c = request.session.get("cart")
        if (c):
            id = list(request.session.get("cart").keys())
            products = Product.get_product_by_id(id)
            return render(request, "cart.html", {"cart": products})
        else:
            noprd = "There no products in the cart. Let's add some products"
            return render(request, "cart.html", {"noprd": noprd})
    
    def post(self, request):
        c = request.session.get("cart")
        prdid = request.POST.get("prdid")
        c.pop(prdid)
        request.session["cart"] = c
        id = list(c.keys())
        if (id == []):
            noprd = "There no products in the cart. Let's add some products"
            return render(request, "cart.html", {"noprd": noprd})
        else:
            products = Product.get_product_by_id(id)
            return render(request, "cart.html", {"cart": products})