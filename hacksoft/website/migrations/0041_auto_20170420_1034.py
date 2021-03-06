# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 10:34
from __future__ import unicode_literals

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0040_blogpost_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='authors',
            field=modelcluster.fields.ParentalManyToManyField(to='website.Teammate'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(to='website.Category'),
        ),
    ]
