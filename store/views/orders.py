from django.shortcuts import render, redirect
from django.views import View
from store.models.order import Order
from store.models.rate import Rate
from store.models.customer import Customer
from store.models.product import Product

class OrderView(View):
    def get(self, request):
        customer = request.session.get("customer_id")
        order = Order.by_customer(customer)
        o = []
        for od in order:
            chk_rate = Rate.check_order_id(od)
            if (chk_rate):
                pass
            else:
                o.append(od)
        return render(request, "orders.html", {"order":o})
    
    def post(self, request):
        o_idd = request.POST.get("o_idd")
        p_idd = request.POST.get("p_idd")
        rating1 = request.POST.get("rate1")
        rating2 = request.POST.get("rate2")
        rating3 = request.POST.get("rate3")
        rating4 = request.POST.get("rate4")
        rating5 = request.POST.get("rate5")
        val = request.POST.get("sub_btn")
        
        customer = request.session.get("customer_id")
        order = Order.get_order_by_id(o_idd)
        orders = Order.by_customer(customer)
        o = []
        for od in orders:
            chk_rate = Rate.check_order_id(od)
            if (chk_rate):
                pass
            else:
                o.append(od)

        if (val == "RATE"):
            flag = 0
            if (rating1 != None):
                flag = 1
            elif (rating2 != None):
                flag = 2
            elif (rating3 != None):
                flag = 3
            elif (rating4 != None):
                flag = 4
            elif (rating5 != None):
                flag = 5
        
            p = Product.get_product(p_idd)
            c = Customer.customer_info(str(customer))
    
            for i in p:
                rate = Rate (
                    rating = flag,
                    product = i,
                    customer = c,
                    order = order
                )
            Rate.place_order(rate)
            Order.rating_update(o_idd, flag)
            return redirect("orders")

        elif (val == "NOT NOW"):
            return render(request, "orders.html", {"order":o, "my_class":"hide_class"})
        
    