# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-28 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20200329_0503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_state',
            name='sp',
        ),
        migrations.AddField(
            model_name='order_state',
            name='number',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
