# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-12 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('package', '0003_created_by_field_removed'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimelineEventInserterRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('AuthorTimelineEventRule', 'Author'), ('TagTimelineEventRule', 'Tag'), ('AfterDatetimeTimelineEventRule', 'After'), ('TitleRegexpTimelineEventRule', 'Title regexp'), ('TitlePrefixTimelineEventRule', 'Title prefix')], max_length=64)),
                ('argument', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TimelineEventInserterRulebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('SteemPostService', 'Steem Post')], max_length=64)),
                ('last', models.CharField(max_length=256, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeline_rulebooks', to='package.Project')),
            ],
        ),
        migrations.AddField(
            model_name='timelineeventinserterrule',
            name='rulebook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='timeline.TimelineEventInserterRulebook'),
        ),
    ]