# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msi', '0004_sessao_url_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessao',
            name='faixa',
            field=models.CharField(default='.png', max_length=100),
        ),
    ]
