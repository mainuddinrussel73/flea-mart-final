# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-22 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='username',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.TextField(max_length=200),
        ),
    ]
