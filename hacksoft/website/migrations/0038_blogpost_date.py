# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-02 15:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0037_blogpost_index_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 3, 2, 15, 37, 5, 376239, tzinfo=utc), verbose_name='Post date'),
            preserve_default=False,
        ),
    ]