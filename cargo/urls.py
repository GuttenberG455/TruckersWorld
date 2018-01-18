
from django.conf.urls import url
from cargo import views

urlpatterns = [
    url(r'^main$', views.mainpage, name="cargo_main"),
    url(r'^addnewfreight$', views.add_new_freight, name="add_new_freight"),
    url(r'^showfreight/(?P<id_freight>\d+)$', views.full_info, name="show_freight"),
]
