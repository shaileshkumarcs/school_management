# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-30 17:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20180630_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=10)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_createdby', to=settings.AUTH_USER_MODEL)),
                ('sessions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_year', to='mainapp.Sessions')),
            ],
        ),
    ]
