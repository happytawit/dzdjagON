# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0002_auto_20150506_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='description',
            field=models.CharField(max_length=250, blank=True),
        ),
    ]
