# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-04 23:31
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='state',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]