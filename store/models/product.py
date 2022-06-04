from django.db import models
from .category import Category
from .brand import Brand
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=2000, blank=True)
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(Category, db_column='type2', on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(0),MaxValueValidator(5)])
    brand = models.CharField(max_length=50, default="")
    gender = models.CharField(max_length=50, default="")
    size = models.CharField(max_length=50, default="")
    
    @staticmethod
    def get_product_by_id(id):
        return Product.objects.filter(id__in = id)
    
    @staticmethod
    def get_product(id):
        return Product.objects.filter(id = id)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_spf_products(category_id):
        if (category_id):
            return Product.objects.filter(category = category_id)
        else:
            return Product.objects.all()
    
    @staticmethod
    def get_brands():
        return Product.objects.values("brand").distinct()

    @staticmethod
    def gen_filter(g, prds):
        if (g == "Male"):
            return prds.filter(gender = g)
        elif (g == "Female"):
            g = "women"
            return prds.filter(gender = g)

    @staticmethod
    def sorting(s, prds):
        if (s == "Low To High"):
            return prds.order_by('price')
        elif (s == "High To Low"):
            return prds.order_by('-price')
    @staticmethod
    def typee(fil, prds):
        return prds.filter(category__in = fil)
    @staticmethod
    def brandfilter(brand, prds):
        return prds.filter(brand__in = brand)