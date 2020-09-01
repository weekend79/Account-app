from django.db import models
from products.models import Product


# Create your models here.
class Order(models.Model):
    full_name = models.CharField(max_length=150, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    postcode = models.CharField(max_length=100, blank=True)
    town_or_city = models.CharField(max_length=100, blank=False)
    street_address1 = models.CharField(max_length=100, blank=False)
    street_address2 = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=100, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)

