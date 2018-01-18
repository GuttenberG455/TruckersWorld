from django.forms import *
from django.contrib.auth import *
from social.models import *
from shop.models import *
from django.contrib.auth.models import User


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('product_truck', 'product_address', 'product_description', 'product_price')
