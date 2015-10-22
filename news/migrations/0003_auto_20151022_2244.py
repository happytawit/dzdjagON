# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150506_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
