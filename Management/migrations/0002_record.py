# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2020-03-11 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20)),
                ('equity', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20)),
                ('open_lots', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='Management.Account')),
            ],
            options={
                'ordering': ('-open_date',),
            },
        ),
    ]