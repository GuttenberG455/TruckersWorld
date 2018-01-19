
from django.conf.urls import url
from social import views

urlpatterns = [
    url(r'^feed$', views.feed, name='social_feed'),
    url(r'^media$', views.media, name='video_feed'),
    url(r'^registration$', views.reg_form, name='registration_form'),
    url(r'^entrance$', views.authorization, name='entrance'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^addnewpost$', views.add_new_post, name='add_new_post'),
    url(r'^personalpage/(?P<id_user>\d+)$', views.personal_page, name='personal_page'),
    url(r'^personaltrucks/(?P<id_user>\d+)$', views.personal_trucks, name='personal_trucks'),
    url(r'^showusers/$', views.show_users, name='show_users'),
    url(r'^editpersonal/(?P<id_user>\d+)$', views.edit_personal, name='edit_personal'),
    url(r'^addcomment/(?P<id_user>\d+)$', views.add_comment, name='add_comment'),
    url(r'^addvideo/$', views.add_video, name='add_video'),
    url(r'^addtruck/$', views.add_truck, name='add_truck'),
    url(r'^edittruck/(?P<id_truck>\d+)$', views.edit_truck, name='edit_truck'),
    url(r'^showvideo/(?P<id_video>\d+)$', views.show_video, name='show_video'),

]
