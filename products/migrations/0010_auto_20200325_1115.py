# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-25 11:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200325_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
