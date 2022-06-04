from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View

class Login(View):
    def get(self, request):
         return render(request, "login.html")

    def post(self, request):
        user = request.POST.get("user")
        password = request.POST.get("password")

        x = user.find("@")
        flag = "email"
        if (x == -1):
            flag = "phone"
        userdata = Customer.checkk(user, flag)

        error = None
        if (not user):
            error = "Enter either phone or email"
        elif (not password):
            error = "enter the password"
        elif (userdata == None):
            error = "enter correct " + flag
        elif (check_password(password, userdata.password) == False):
            error = "enter the correct password"
        
        if (error == None):
            request.session["customer_id"] = userdata.id
            if (flag == "email"):
                request.session["customer_user"] = userdata.email
            elif (flag == "phone"):
                request.session["customer_user"] = userdata.phone

            return redirect("main") 
        else:
            data = {
                "error": error,
                "user": user
            }
            return render(request, "login.html", data)

def logout(request):
    request.session.clear()
    return  redirect("login")