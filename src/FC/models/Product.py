from django.db import models
from ProductCategory import ProductCategory
from ProductDiscount import ProductDiscount

class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory)
    product_discount = models.ManyToManyField(ProductDiscount, through = 'ProductDiscountItem')
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    image_url = models.CharField(max_length = 250)
    visibility = models.BooleanField()
    description = models.TextField()
    presentation_index = models.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'FC'
