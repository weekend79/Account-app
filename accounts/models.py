from django.db import models


# My models
class UserProfile(models.Model):
    full_name = models.CharField(max_length=200, default='')
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    postnumber = models.CharField(max_length=6, blank=True)
    postaddress = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    propic = models.ImageField(upload_to='images/', default="")

    def __str__(self):
        return self.name

