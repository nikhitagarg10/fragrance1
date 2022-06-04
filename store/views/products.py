from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

class Products(View):
    def post(self, request):
        amt = request.POST.get("amount")
        prd_id = request.POST.get("prdid")
        if (prd_id != None):
            p_obj = Product.get_product(prd_id)
            cat = p_obj[0].category
            type2 = Category.get_category_type2(cat)

            cart = request.session.get("cart")  
            if cart:
                q = cart.get(prd_id)
                if q:
                    q = int(q) + int(amt)
                else:
                    q = amt
                cart[prd_id] = q
            else:
                cart = {} 
                cart[prd_id] = amt
            
            request.session["cart"] = cart
        return render(request, "products.html", {"product":p_obj[0], "cat_type":type2})
        
    def get(self, request):
        product_id = request.GET.get("product_id")
        if (product_id != None):
            p_obj = Product.get_product(product_id)
            cat = p_obj[0].category
            type2 = Category.get_category_type2(cat)
        return render(request, "products.html", {"product":p_obj[0], "cat_type":type2})