# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('technical_data_sheet', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=200)),
                ('first_img', models.ImageField(upload_to='')),
            ],
        ),
    ]
