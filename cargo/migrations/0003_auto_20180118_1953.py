# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-18 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0002_auto_20180117_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freight',
            name='freight_height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='freight',
            name='freight_length',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='freight',
            name='freight_width',
            field=models.FloatField(blank=True, null=True),
        ),
    ]