# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-08-23 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arya_lib', '0004_auto_20160822_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField(max_length=10)),
                ('bookname', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=30)),
            ],
        ),
    ]
