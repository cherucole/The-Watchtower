# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 08:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20181019_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='biz_hood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biz', to='app.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='user_profile',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='hoods', to=settings.AUTH_USER_MODEL),
        ),
    ]
