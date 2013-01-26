from django.db import models
from Product import Product
from ProductDiscount import ProductDiscount

class ProductDiscountItem(models.Model):
    product = models.ForeignKey(Product)
    product_discount = models.ForeignKey(ProductDiscount)

    class Meta:
        app_label = 'FC'
