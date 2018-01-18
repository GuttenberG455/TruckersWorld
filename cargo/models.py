import django
from django.db import models
from shop.models import *
from social.models import *

from social.models import User


class Freight(models.Model):
    freight_id = models.AutoField(primary_key=True)
    freight_description = models.CharField(max_length=40)
    freight_comment = models.TextField(max_length=150, blank=True)
    freight_category = models.CharField(max_length=30)
    freight_length = models.FloatField(blank=True, null=True)
    freight_width = models.FloatField(blank=True, null=True)
    freight_height = models.FloatField(blank=True, null=True)
    freight_weight = models.FloatField()
    freight_first_date = models.DateField()
    freight_latest_date = models.DateField()
    freight_address_start = models.CharField(max_length=255)
    freight_address_finish = models.CharField(max_length=255)

    def __str__(self):
        return str(self.freight_id) + self.freight_description


class DeliveryContract(models.Model):
    dlvcontract_id = models.AutoField(primary_key=True)
    dlvcontract_driver = models.ForeignKey(UserPersonal)
    dlvcontract_freight = models.ForeignKey(Freight)
    dlvcontract_consumer = models.CharField(max_length=64)
    dlvcontract_date_receive = models.DateField()
    dlvcontract_time_receive = models.TimeField()
    dlvcontract_delivery_date = models.DateField()
    dlvcontract_delivery_time = models.TimeField()

    def __str__(self):
        return str(self.dlvcontract_id)

