# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 03:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msi', '0013_auto_20171025_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='category',
        ),
        migrations.RemoveField(
            model_name='film',
            name='sessions',
        ),
        migrations.AddField(
            model_name='categ',
            name='filme',
            field=models.ForeignKey(default=30, on_delete=django.db.models.deletion.CASCADE, to='msi.Film'),
        ),
        migrations.AddField(
            model_name='sessao',
            name='filme',
            field=models.ForeignKey(default=30, on_delete=django.db.models.deletion.CASCADE, to='msi.Film'),
        ),
    ]
