from django.shortcuts import render, redirect

from shop.models import *
from cargo.models import *
from social.models import *
from shop.forms import *
# Create your views here.


def main_page(request):
    prod_list = reversed(Product.objects.all())
    return render(request, "shop/main.html", locals())


def add_new_product(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("shop_main")
        else:
            return render(request, "shop/addnewproduct.html", locals())
    return render(request, "shop/addnewproduct.html", locals())


def show_product(request, id_prod):
    prod = Product.objects.get(pk=id_prod)
    return render(request, "shop/showproduct.html", locals())


def buy_product(request, id_prod):
    prod = Product.objects.get(pk=id_prod)
    truck = Truck.objects.get(pk=prod.product_truck_id)
    if request.method == "POST":
        if 'Yes' in request.POST.keys() and request.POST['Yes']:
            print(truck.truck_owner_id)
            print(request.user.id)
            truck.truck_owner = request.user
            truck.save()
            Product.objects.get(pk=id_prod).delete()
            return redirect("personal_trucks", request.user.id)
        else:
            return redirect("show_product", id_prod)
    return render(request, "shop/buy_truck.html", locals())
