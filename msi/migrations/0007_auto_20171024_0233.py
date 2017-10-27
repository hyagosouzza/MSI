# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 04:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msi', '0006_auto_20171024_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categ',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='sessao',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msi.Categ'),
        ),
    ]