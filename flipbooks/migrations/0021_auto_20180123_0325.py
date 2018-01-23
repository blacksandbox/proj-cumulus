# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-23 03:25
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields
import flipbooks.models


class Migration(migrations.Migration):

    dependencies = [
        ('flipbooks', '0020_auto_20180114_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frame',
            name='frame_image_native',
        ),
        migrations.AlterField(
            model_name='frame',
            name='frame_image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=flipbooks.models.frame_upload_path),
        ),
    ]