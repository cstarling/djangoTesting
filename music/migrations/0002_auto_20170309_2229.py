# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 22:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='artists',
            new_name='artist',
        ),
    ]