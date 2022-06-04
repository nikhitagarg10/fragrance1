from django.db import models
from .product import Product
from .customer import Customer
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=500) 
    adress = models.CharField(max_length=50, default="", blank=True)
    phone = models.CharField(max_length=10, default="", blank=True)
    date = models.DateField(default=timezone.now())
    status = models.TextField(max_length=50, default="received")
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(5)])

    @staticmethod
    def place_order(self):
        self.save()
    
    @staticmethod
    def get_order_by_id(id):
        return Order.objects.get(id = id)

    @staticmethod
    def status_update(id, stat):
        o = Order.objects.get(id = id)
        o.status = stat
        o.save()
    
    @staticmethod
    def rating_update(id, rate):
        o = Order.objects.get(id = id)
        o.rating = rate
        o.save()
    
    @staticmethod
    def by_customer(customer):
        return Order.objects.filter(customer = customer).order_by("date").reverse()
    
    @staticmethod
    def get_all_orders():
        return Order.objects.all()
    
    @staticmethod
    def total(o):
        return (int(o.quantity) * int(o.price))
