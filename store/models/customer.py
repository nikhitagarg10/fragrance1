from django.db import models 

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, default="")
    password = models.CharField(max_length=150)

    def register(self):
        self.save()
    
    def customer_info(id):
        return Customer.objects.get(id = id)
        
    def checkk(user, flag):
        if (flag == "email"):
            try:
                return Customer.objects.get(email = user)
            except:
                return None
        elif (flag == "phone"):
            try:
                return Customer.objects.get(phone = user)
            except:
                return None
    def info(email):
       return Customer.objects.get(email=email) 