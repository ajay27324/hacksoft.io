# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-20 14:52
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20160916_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='howweworkpage',
            name='what_we_do_content',
            field=wagtail.wagtailcore.fields.StreamField((('what_we_do_content', wagtail.wagtailcore.blocks.StreamBlock((('title', wagtail.wagtailcore.blocks.RichTextBlock()), ('description', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())))),)),
        ),
    ]
