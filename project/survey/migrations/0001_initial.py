# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 00:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=False)),
                ('reg_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date registrated')),
                ('lang', models.IntegerField(choices=[(0, 'Spanish'), (1, 'English')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date registrated')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Answer')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Question'),
        ),
    ]