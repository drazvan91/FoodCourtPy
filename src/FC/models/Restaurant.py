from django.db import models
from User import User

class Restaurant(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = models.CharField(max_length = 50)
    website = models.URLField()
    admins = models.ManyToManyField(User, through = 'RestaurantAdmin')

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'FC'
