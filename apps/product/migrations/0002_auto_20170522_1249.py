# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-22 12:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 22, 12, 49, 13, 361000), verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]