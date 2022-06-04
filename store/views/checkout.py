from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from store.models.product import Product
from store.models.order import Order

#razor-pay


class CheckOut(View):
    def post(self, request):
        status = " "
        adress = request.POST.get("adress")
        total = request.POST.get("total")
        cart = request.session.get("cart")
        product_id = Product.get_product_by_id(list(cart.keys()))
        
        if (adress == ""):
            status = "please enter your adress for placing the order"
            return render(request, "cart.html", {"status": status, "type": False, "cart": product_id})
        else:
            customer = request.session.get("customer_id")
            customer_info = Customer.customer_info(str(customer))
            
            for p in product_id:
                info = Order(
                    product = p,
                    customer =  customer_info,
                    quantity =  cart.get(str(p.id)),
                    price =  p.price,
                    adress =  adress,
                    phone =  customer_info.phone,
                )
                Order.place_order(info)
           
            request.session["cart"] = {}
            return render(request, 'pay.html',{"p":product_id, "total":int(total)})
