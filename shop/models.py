from django.db import models
from cargo.models import *
from social.models import *
# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_truck = models.ForeignKey(Truck)
    product_address = models.TextField(max_length=200)
    product_description = models.TextField(max_length=300, blank=True)
    product_price = models.FloatField()

    def __str__(self):
        return str(self.product_truck) + ' ' + str(self.product_address)
