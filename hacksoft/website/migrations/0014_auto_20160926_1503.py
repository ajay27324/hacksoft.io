# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-26 15:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_projectpage_project'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectPage',
            new_name='ProjectOPage',
        ),
    ]