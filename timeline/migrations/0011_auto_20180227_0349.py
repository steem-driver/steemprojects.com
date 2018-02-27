# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-27 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0010_auto_20180217_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='timelineeventinserterrulebook',
            name='notify',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='timelineeventinserterrule',
            name='type',
            field=models.CharField(choices=[('SteemAuthorTimelineEventRule', 'Published by'), ('SteemTagTimelineEventRule', 'Has a tag'), ('SteemTitlePrefixTimelineEventRule', 'Title starts with'), ('SteemTitleContainsTimelineEventRule', 'Title contains')], max_length=64),
        ),
        migrations.AlterField(
            model_name='timelineeventinserterrulebook',
            name='last',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]