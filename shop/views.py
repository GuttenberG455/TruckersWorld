from django.shortcuts import render
from shop.models import *
from cargo.models import *
from social.models import *
# Create your views here.


def main_page(request):
    prod_list = reversed(Product.objects.all())
    return render(request, "shop/main.html", locals())


def add_new_product(request):
    return render(request, "shop/addnewproduct.html", locals())


def show_product(request, id_prod):
    prod = Product.objects.get(pk=id_prod)
    return render(request, "shop/showproduct.html", locals())
