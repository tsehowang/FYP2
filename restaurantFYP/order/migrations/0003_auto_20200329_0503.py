# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-28 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200329_0453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_state',
            old_name='food_id',
            new_name='food',
        ),
        migrations.RenameField(
            model_name='order_state',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RemoveField(
            model_name='order_state',
            name='state',
        ),
        migrations.AddField(
            model_name='order_state',
            name='sp',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
