# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0002_auto_20170703_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='win',
            field=models.BooleanField(default=True),
        ),
    ]
