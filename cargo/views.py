from django.shortcuts import render, redirect
from social.models import *
from cargo.models import *
from cargo.forms import *
# Create your views here.


def mainpage(request):
    freight_list = Freight.objects.all()
    freight_list = reversed(freight_list)
    return render(request, "cargo/main.html", locals())


def add_new_freight(request):
    form = FreightForm(request.POST or None)
    # print(request.method)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("cargo_main")
        else:
            return render(request, "cargo/addnewfreight.html", locals())
    return render(request, "cargo/addnewfreight.html", locals())


def full_info(request, id_freight):
    freight = Freight.objects.get(freight_id=id_freight)
    return render(request, "cargo/fullinfo.html", locals())
