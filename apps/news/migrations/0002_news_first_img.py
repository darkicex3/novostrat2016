# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 18:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='first_img',
            field=models.ImageField(default=datetime.datetime(2016, 3, 16, 18, 26, 10, 427049, tzinfo=utc), upload_to=''),
            preserve_default=False,
        ),
    ]
