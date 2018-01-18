from django.db import models
from shop.models import *
from cargo.models import *
from django.contrib.auth.models import User, Group
# Create your models here.


class UserGroup(models.Model):
    group_django = models.OneToOneField(Group, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=64)
    group_bool_moderator = models.BooleanField()

    def __str__(self):
        return self.group_name


class UserPersonal(models.Model):
    user_django = models.OneToOneField(User, on_delete=models.CASCADE)
    user_id = models.AutoField(primary_key=True)
    user_group_id = models.ForeignKey(UserGroup)
    user_name = models.CharField(max_length=24, blank=True)
    user_surname = models.CharField(max_length=48, blank=True)
    user_gender = models.CharField(max_length=1, blank=True)
    user_dateofbirth = models.DateField(null=True, blank=True)
    user_company_name = models.CharField(max_length=128, blank=True)
    user_phone_number = models.CharField(max_length=13, blank=True)
    user_image = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return str(self.user_id) + " " + str(self.user_django)

    def str_user(self):
        return self.user_name + ' ' + self.user_surname

    def str_company(self):
        return self.user_company_name


class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    title_post = models.CharField(max_length=40)
    text_post = models.TextField(max_length=512)
    image1_post = models.CharField(max_length=1000, blank=True)
    image2_post = models.CharField(max_length=1000, blank=True)
    image3_post = models.CharField(max_length=1000, blank=True)
    image4_post = models.CharField(max_length=1000, blank=True)
    image5_post = models.CharField(max_length=1000, blank=True)
    author_post = models.ForeignKey(UserPersonal, blank=True, null=True)

    def __str__(self):
        return str(self.id_post) + " " + self.title_post


class Truck(models.Model):
    truck_id = models.AutoField(primary_key=True)
    truck_brend = models.CharField(max_length=48)
    truck_model = models.CharField(max_length=48)
    truck_release_year = models.IntegerField()
    truck_type = models.CharField(max_length=48)
    truck_mileage = models.IntegerField()
    truck_gosnum = models.CharField(max_length=15, blank=True)
    truck_vinnum = models.CharField(max_length=20)
    truck_engine = models.CharField(max_length=48)
    truck_engine_vol = models.FloatField()
    truck_engine_power = models.FloatField()
    truck_wheel_formula = models.CharField(max_length=3)
    truck_owner = models.ForeignKey(User, null=True, blank=True)
    truck_image = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.truck_brend + ' ' + self.truck_model + ' ' + str(self.truck_release_year)

    def str_full(self):
        return self.truck_brend + ' ' + self.truck_model + ' ' + self.truck_vinnum


class Video(models.Model):
    video_id = models.AutoField(primary_key=True)
    video_link = models.CharField(max_length=1000)
    video_name = models.CharField(max_length=64)
    video_description = models.TextField(max_length=512, blank=True)
    video_author = models.ForeignKey(UserPersonal, blank=True, null=True)

    def __str__(self):
        return str(self.video_id) + self.video_name


class Commentary(models.Model):
    commentary_id = models.AutoField(primary_key=True)
    commentary_text = models.TextField(max_length=300)
    commentary_author = models.ForeignKey(UserPersonal, blank=True, null=True)
    commentary_link = models.CharField(max_length=127)
    commentary_date = models.DateField(auto_created=True)


