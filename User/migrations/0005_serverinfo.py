# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-24 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_comments_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]
