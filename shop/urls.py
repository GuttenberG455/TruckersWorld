from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^main$', views.main_page, name="shop_main"),
    url(r'^addnewproduct$', views.add_new_product, name="add_new_product"),
    url(r'^showproduct/(?P<id_prod>\d+)$', views.show_product, name="show_product"),
]
