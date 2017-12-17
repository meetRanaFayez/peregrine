# -*- coding: utf-8 -*-
# Generated by Django 1.11.8.dev20171216134037 on 2017-12-16 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('peregrine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeregrineSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_number', models.IntegerField(default=10, help_text='The number of posts to display.')),
                ('post_number_nav', models.IntegerField(default=10, help_text='The number of posts to display in navigation.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255, unique=True)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddIndex(
            model_name='settings',
            index=models.Index(fields=['key'], name='settings_key_idx'),
        ),
        migrations.AddField(
            model_name='peregrinesettings',
            name='landing_page',
            field=models.ForeignKey(blank=True, help_text='The page to display at the root. If blank, displays latest posts.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='peregrinesettings',
            name='site',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site'),
        ),
    ]
