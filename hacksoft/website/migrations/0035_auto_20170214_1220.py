# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_auto_20170129_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=models.TextField(),
        ),
    ]