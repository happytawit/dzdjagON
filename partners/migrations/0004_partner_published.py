# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_auto_20150506_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
