from django.db import models
from Restaurant import Restaurant
from ProductCategoryDiscount import ProductCategoryDiscount

class ProductCategory(models.Model):

    restaurant = models.ForeignKey(Restaurant)
    product_category_discount = models.ManyToManyField(
        ProductCategoryDiscount, through = 'ProductCategoryDiscountItem')
    name = models.CharField(max_length = 50)
    presentation_index = models.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'FC'
