# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msi', '0014_auto_20171025_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categ',
            name='filme',
        ),
        migrations.AddField(
            model_name='categ',
            name='filme',
            field=models.ManyToManyField(to='msi.Film'),
        ),
        migrations.RemoveField(
            model_name='sessao',
            name='filme',
        ),
        migrations.AddField(
            model_name='sessao',
            name='filme',
            field=models.ManyToManyField(to='msi.Film'),
        ),
    ]