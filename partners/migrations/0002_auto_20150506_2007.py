# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='partner_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='partner',
            old_name='partner_name',
            new_name='name',
        ),
    ]
