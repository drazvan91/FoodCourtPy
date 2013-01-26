from django.db import models

class ProductDiscount(models.Model):
    name = models.CharField(max_length = 50)
    price = models.IntegerField()
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'FC'
