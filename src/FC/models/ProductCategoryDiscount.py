from django.db import models

class ProductCategoryDiscount(models.Model):
    name = models.CharField(max_length = 50)
    price = models.IntegerField()
    description = models.TextField()

    class Meta:
        app_label = 'FC'
