# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-08-02 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arya_lib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_login_list',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
