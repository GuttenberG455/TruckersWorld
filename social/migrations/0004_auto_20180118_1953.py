# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-18 16:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20180117_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentary',
            name='commentary_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.UserPersonal'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.UserPersonal'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='truck_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.UserPersonal'),
        ),
    ]