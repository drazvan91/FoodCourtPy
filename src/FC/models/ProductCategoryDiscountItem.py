from django.db import models
from ProductCategory import ProductCategory
from ProductCategoryDiscount import ProductCategoryDiscount

class ProductCategoryDiscountItem(models.Model):
    product_category = models.ForeignKey(ProductCategory)
    product_category_discount = models.ForeignKey(ProductCategoryDiscount)

    class Meta:
        app_label = 'FC'
