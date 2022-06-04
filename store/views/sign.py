from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, "signup.html")
    
    def post(self, request):

        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        pnum = request.POST.get("pnum")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        checkbox = request.POST.get("checkbox")
    
        value = {
            "fname": fname, "lname": lname,
            "pnum": pnum, "email": email }

        error = self.validatemethod(fname, lname, pnum, email, gender, password1, password2, checkbox)
        
        if (error == None):
            customer = Customer(first_name=fname, last_name=lname, email=email, phone=pnum,  gender=gender, password=password1)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect("login")
        else:
            data = {
                "error": error,
                "values": value
            }
            return render(request, "signup.html", data)
    
    def validatemethod(self, fname, lname, pnum, email, gender, password1, password2, checkbox):
        error = None 

        if (not fname):
            error = "first name required"
        elif (not lname):
            error = "last name required"
        elif (not pnum):
            error = "phone number is required"
        elif (len(pnum) != 10):
            error = "phone number is invalid"
        elif (not email):
                error = "email is required"
        elif (not gender):
                error = "gender is required"
        elif(not password1):
            error = "password is must"
        elif(password1 != password2):
            error = "passwords do not match"
        elif (len(password1) < 7):
            error = "password needs to be of 7 characters or more"
        elif(checkbox == None):
            error = "agree to the terms and conditions"
        elif (pnum):
            p = Customer.objects.filter(phone=pnum)
            if (p):
                error = "An account already exists with this phone number"
        elif (email):
            e = customer.objects.filter(email=email)
            if (e):
                error = "An account already exists with this email"
        return error
