# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-19 10:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('package', '0001_initial'),
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dpotw',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.Project'),
        ),
    ]
