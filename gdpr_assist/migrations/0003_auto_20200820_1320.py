# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-20 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gdpr_assist', '0002_auto_20200727_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlog',
            name='target_pk',
            field=models.TextField(null=True),
        ),
    ]