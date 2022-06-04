from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    class Type1(models.IntegerChoices):
        woody = 1
        floral = 2
        oriental = 3
        fresh = 4
        celebrity_scents = 5

    type1 = models.IntegerField(choices = Type1.choices, null=True)
    class Type2(models.IntegerChoices):
        fresh_floral = 1
        fruity_floral = 2
        oriental_floral = 3
        classic_oriental = 4
        woody_oriental = 5
        fresh_water = 6
        fresh_citrus = 7
        fresh_green = 8
        woody_mossy = 9
        woody_smokey = 10
        celebrity_scents = 11
        fresh_oriental = 12
    type2 = models.IntegerField(choices = Type2.choices,  null=True)


    @staticmethod
    def get_all_category():
        return Category.objects.all()
    
    @staticmethod
    def get_category_type():
        t = set()
        cat = Category.objects.all()
        for c in cat:
            x = c.get_type1_display()
            t.add(x)
        return t
    
    @staticmethod
    def get_category_type2(cat):
        return cat.get_type2_display()

    @staticmethod
    def get_cat_num(category):
        cat_ty = []
        cat = Category.objects.all()
        for c in cat:
            if (c.get_type1_display() == category):
                cat_ty.append(c.id)
        return cat_ty

    '''@staticmethod
    def get_cat_id(cat):
        return Category.objects.filter(type1 = cat)'''
        