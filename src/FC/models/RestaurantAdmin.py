from django.db import models
from Restaurant import Restaurant
from User import User

class RestaurantAdmin(models.Model):
    user_id = models.ForeignKey(User)
    restaurant_id = models.ForeignKey(Restaurant)
    ROLE_CHOICES = [(u'M', u'Moderator'), (u'A', u'Admin')]
    role = models.CharField(max_length = 50, choices = ROLE_CHOICES)

    def __unicode__(self):
        return str(self.user_id) + " " + str(self.restaurant_id)

    class Meta:
        app_label = 'FC'
        unique_together = ('user_id', 'restaurant_id')
