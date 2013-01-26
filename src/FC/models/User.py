from django.db import models
import hashlib

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    signup_date = models.DateTimeField()
    email = models.EmailField()
    password_md5 = models.CharField(max_length = 100)
    password_salt = models.IntegerField()

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def checkPassword(self, password):
        ch = hashlib.md5(password + str(self.password_salt)).hexdigest()
        return ch == self.password_md5

    class Meta:
        app_label = 'FC'
