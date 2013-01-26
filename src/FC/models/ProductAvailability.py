from django.db import models
from Product import Product

class ProductAvailability(models.Model):
    product = models.ForeignKey(Product)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        app_label = 'FC'
